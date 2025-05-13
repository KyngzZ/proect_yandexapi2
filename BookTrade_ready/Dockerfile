FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN flask db init || true
RUN flask db migrate -m "init" || true
RUN flask db upgrade
RUN python scripts/seed_data.py
EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "run:app"]