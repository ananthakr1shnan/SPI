FROM python:3.8-slim-buster
WORKDIR /app
COPY pyproject.toml /app/

RUN pip install --upgrade pip setuptools wheel && \
    pip install .

COPY . /app

EXPOSE 5000

CMD ["python", "app.py"]
