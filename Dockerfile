# FROM python:3.13-slim
# WORKDIR /app
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt
# COPY . .
# EXPOSE 8051
# ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8051", "--server.address=0.0.0.0"]



# Stage 1: Builder with uv
FROM ghcr.io/astral-sh/uv:0.1.11-python3.11-slim AS builder
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv venv && .venv/bin/uv sync --locked
COPY . .
ENV UV_COMPILE_BYTECODE=1
RUN .venv/bin/uv sync

# Stage 2: Runtime image
FROM python:3.13-slim
WORKDIR /app
COPY --from=builder /app /app
ENV PATH="/app/.venv/bin:$PATH"
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]