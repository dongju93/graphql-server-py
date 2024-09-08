FROM python:3.12.5-slim

WORKDIR /graphql

RUN apt update && apt install -y \
    tzdata \
    && ln -fs /usr/share/zoneinfo/Asia/Seoul /etc/localtime \
    && dpkg-reconfigure -f noninteractive tzdata \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

COPY . /graphql

RUN pip install poetry

RUN poetry config virtualenvs.create false \
    && poetry install --only main --no-root

EXPOSE 8200

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8200"]
