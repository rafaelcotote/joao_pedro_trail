FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /tmp/pygbag_app \
    && cp main.py /tmp/pygbag_app/main.py \
    && python -m pygbag --build /tmp/pygbag_app

FROM python:3.11-slim

WORKDIR /app

COPY --from=builder /tmp/pygbag_app/build/web /app/web

EXPOSE 8085

CMD ["python", "-m", "http.server", "8085", "--directory", "/app/web"]
