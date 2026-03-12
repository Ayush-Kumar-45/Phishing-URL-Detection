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

# List files to verify model is copied
RUN echo "=== FILES IN /APP ===" && ls -la /app/
RUN echo "=== FILES IN UTILS ===" && ls -la /app/utils/ || echo "utils directory not found"
RUN echo "=== CHECKING MODEL FILE ===" && ls -la /app/*.pkl || echo "No .pkl files found"

# Ensure model file has correct permissions
RUN chmod 644 /app/phishing_model.pkl || echo "Model file not found for chmod"

# Expose port
EXPOSE 10000

# Run the application
CMD gunicorn app:app --bind 0.0.0.0:$PORT --workers 4 --timeout 120
