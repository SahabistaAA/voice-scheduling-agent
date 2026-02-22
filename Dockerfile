FROM node:20 AS builder

WORKDIR /app/ui
# Copy package.json and install to leverage docker cache
COPY source/ui/package*.json ./
RUN npm install

# Copy source and build
COPY source/ui/ ./
RUN npm run build

# Stage 2: Python Backend
FROM python:3.10-slim

WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy dependency files
COPY pyproject.toml /app/

# Install dependencies using uv into the system python
RUN uv pip install --system -r pyproject.toml

# Copy the rest of the application
COPY . /app/

# Copy the built React app from the builder stage
COPY --from=builder /app/ui/dist /app/source/ui/dist

EXPOSE 8000

CMD ["sh", "-c", "uvicorn api.index:app --host 0.0.0.0 --port ${PORT:-8000}"]
