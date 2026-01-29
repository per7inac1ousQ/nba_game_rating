FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1

# Copy requirements first for better caching
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY nba_server.py .

RUN useradd -m -u 1000 mcpuser && chown -R mcpuser:mcpuser /app

USER mcpuser

CMD ["python", "nba_server.py"]