# Use Python 3.9 slim image (stable and compatible)
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies needed for numpy/scikit-learn
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for better caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir setuptools wheel \
    && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Create logs directory
RUN mkdir -p logs

# Expose port (Render uses PORT env variable)
EXPOSE 10000

# Run the application with gunicorn
CMD gunicorn app:app --bind 0.0.0.0:$PORT --workers 4 --timeout 120
