
FROM python:3.12-slim
WORKDIR /app
RUN pip install --no-cache-dir uv
COPY pyproject.toml uv.lock ./
RUN uv sync --no-dev
COPY main.py app.py ./
EXPOSE 8000

# uv tworzy wirtualne środowisko w katalogu .venv,
# więc używamy go do uruchomienia aplikacji, można to wyłączyć,
# to jest wygodniejsze
CMD [".venv/bin/python3", "main.py"]




