up:
	docker compose -f docker-compose.yml up --build -d

build:
	docker compose -f docker-compose.yml build

down:
	docker compose -f docker-compose.yml down

logs:
	docker compose -f docker-compose.yml logs -f

setup:
	poetry install --no-root

test-unit:
	poetry run pytest -q tests/unit

test-integration:
	poetry run pytest -q tests/integration

test:
	poetry run pytest -q tests

run:
	poetry run uvicorn app.interfaces.main:app --host 0.0.0.0 --port 8000 --reload

migrate:
	poetry run alembic upgrade head

revision:
	poetry run alembic revision -m "init schema" --autogenerate

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete

