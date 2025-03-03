# Use Python base image
FROM python:3.13

WORKDIR /app

COPY app /app

RUN pip install --no-cache-dir -r /app/requirements.txt

EXPOSE 8080
EXPOSE 7687

CMD ["python", "app.py"]

