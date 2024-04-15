
# Backend commands.
CMD:=poetry run
backend:=cd backend
get-poetry:
	curl -sSL https://install.python-poetry.org | python3 -
migrate:
	$(backend) && $(CMD) python3 manage.py makemigrations
	$(backend) && $(CMD) python3 manage.py migrate
user:
	$(backend) && $(CMD) python3 manage.py createsuperuser

# Frontend commands.
frontend:=cd frontend

# Commands works on both servers.
install:
	$(backend) && poetry install
	$(backend) && poetry check
	$(frontend) && yarn

run:
ifeq ($(server), frontend)
	$(frontend) && yarn dev
else ifeq ($(server), backend)
	$(backend) && $(CMD) python3 manage.py runserver
endif

lint:
	$(backend) && $(CMD) black .  --exclude=__init__.py
	$(backend) && $(CMD) flake8 .  --exclude=__init__.py
	# $(frontend) && yarn lint

# Run examples
# Python Example
py-switchkeys:
	cd clients/python && python3 -m example

# Dart Example
dart-switchkeys:
	cd clients/dart/switchkeys && dart example.dart

# Typescript Example
ts-switchkeys:
	cd clients/typescript && npx ts-node ./example.ts

# Docker commands
docker-up:
ifeq ($(service), backend)
	docker compose -f ./docker/docker-compose.yml --env-file=./config/.env up backend --build -d
# else ifeq ($(service), frontend) | docker compose -f ./docker/docker-compose.yml --env-file=./config/.env up frontend --build -d
else ifeq ($(service), postgres)
	docker compose -f ./docker/docker-compose.yml --env-file=./config/.env up postgres --build -d
else
	docker compose -f ./docker/docker-compose.yml --env-file=./config/.env up --build -d
endif

docker-down:
ifeq ($(service), backend)
	docker compose -f ./docker/docker-compose.yml --env-file=./config/.env down backend
# else ifeq ($(service), frontend) | docker compose -f ./docker/docker-compose.yml --env-file=./config/.env down frontend
else ifeq ($(service), postgres)
	docker compose -f ./docker/docker-compose.yml --env-file=./config/.env down postgres
else
	docker compose -f ./docker/docker-compose.yml --env-file=./config/.env down
endif

docker-logs:
ifeq ($(service), backend)
	docker compose -f ./docker/docker-compose.yml --env-file=./config/.env logs -f backend
# else ifeq ($(service), frontend) | docker compose -f ./docker/docker-compose.yml --env-file=./config/.env logs -f frontend
else ifeq ($(service), postgres)
	docker compose -f ./docker/docker-compose.yml --env-file=./config/.env logs -f postgres
else
	docker compose -f ./docker/docker-compose.yml --env-file=./config/.env logs -f
endif

