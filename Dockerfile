FROM python:3.12.1-slim-bullseye
WORKDIR /app/
COPY poetry.lock pyproject.toml /app/
RUN pip install --upgrade pip \
    && pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi
COPY . /app
RUN chown -R 1000:1000 /app
EXPOSE 8000
RUN chmod +x app/runner/*.sh
ENTRYPOINT ./runner/django_run.sh
