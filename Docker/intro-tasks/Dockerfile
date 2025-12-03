FROM python:3.8-slim

WORKDIR /app

COPY . .

# Install system packages needed for mysqlclient
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
 && pip install --no-cache-dir flask mysqlclient \
 && rm -rf /var/lib/apt/lists/*

EXPOSE 5000
CMD ["python", "app.py"]
