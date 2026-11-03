FROM python:3.11-slim

WORKDIR /app

COPY index.html game.js ./

EXPOSE 8085

CMD ["python", "-m", "http.server", "8085", "--directory", "/app"]
