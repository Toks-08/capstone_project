#!/usr/bin/env bash

poetry install --no-interaction --no-ansi

poetry run python manage.py collectstatic --noinput
poetry run python manage.py migrate
