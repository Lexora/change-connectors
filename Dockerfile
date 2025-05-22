# Use an official Python image
FROM python:3.13-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install Poetry
RUN pip install --no-cache-dir poetry

# Copy dependency definitions first (for better caching)
COPY pyproject.toml poetry.lock* /app/

# Install dependencies (no virtualenv, installs into container env)
RUN poetry config virtualenvs.create false \
 && poetry install --no-root --no-interaction --no-ansi

# Copy the rest of the application code
COPY . /app

# Default command (edit as needed)
CMD ["python", "change_connectors.py"]
