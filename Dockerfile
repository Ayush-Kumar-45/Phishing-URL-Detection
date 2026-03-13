FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir setuptools wheel \
    && pip install --no-cache-dir -r requirements.txt

# Copy the entire application
COPY . .

# Create logs directory
RUN mkdir -p logs

# Debug: List all files to verify model is copied
RUN echo "\n=== CONTAINER FILE STRUCTURE ===" && \
    echo "\n=== Files in /app ===" && \
    ls -la /app/ && \
    echo "\n=== Files in /app/utils ===" && \
    ls -la /app/utils/ || echo "utils directory not found" && \
    echo "\n=== Looking for .pkl files ===" && \
    find /app -name "*.pkl" -o -name "*.pkl.gz" | xargs ls -la || echo "No .pkl files found" && \
    echo "\n=== File sizes ===" && \
    du -sh /app/* 2>/dev/null || true

# Set permissions
RUN chmod -R 755 /app

# Expose port
EXPOSE 10000

# Run the application
CMD gunicorn app:app --bind 0.0.0.0:$PORT --workers 2 --timeout 120 --log-level debug
