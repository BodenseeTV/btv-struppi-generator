# syntax=docker/dockerfile:1

# =========================
# Builder Stage
# =========================
FROM python:3.14-slim AS builder

# Python-Optimierungen
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# uv Binary kopieren
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Dependency-Dateien zuerst kopieren
# -> besseres Docker Layer Caching
COPY pyproject.toml uv.lock ./

# Virtuelle Umgebung + Dependencies installieren
RUN uv sync --frozen --no-dev

# Restliches Projekt kopieren
COPY . .

RUN ls

# Falls das Projekt selbst als Package installiert werden muss
RUN uv sync --frozen --no-dev


# =========================
# Runtime Stage
# =========================
FROM python:3.14-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/app/.venv/bin:$PATH"

WORKDIR /app
COPY --from=builder /app /app

RUN ls

CMD ["python", "src/main.py"]