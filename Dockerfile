FROM python:3.9-slim

WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .
COPY blood_bank_logic.py .
COPY templates/ ./templates/

# Expose the port Flask runs on
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
