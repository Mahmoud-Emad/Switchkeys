
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

switchkey:
	cd clients/py && python3 -m example