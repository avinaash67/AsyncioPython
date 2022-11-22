FROM python:3.7-alpine3.15
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY src src

# Checks for the app integrity by requesting the endpoint '/health' 
HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
            CMD curl -f http://localhost/health || exit 1

ENTRYPOINT [ "python", "./src/app.py" ]
EXPOSE 5000
