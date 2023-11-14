FROM --platform=linux/amd64 ghcr.io/owl-corp/python-poetry-base:3.11-slim

COPY pyproject.toml poetry.lock ./
RUN poetry install

COPY . .

ENTRYPOINT ["poetry"]
CMD ["run", "python", "-OO", "-m", "oleg"]