
# Backend commands.
CMD:=poetry run
backend:=cd backend
get-poetry:
	curl -sSL https://install.python-poetry.org | python3 -
migrate:
	$(backend) && $(CMD) python3 manage.py makemigrations
	$(backend) && $(CMD) python3 manage.py migrate
user:
	$(server) && $(CMD) python3 manage.py createsuperuser

# Commands works on both servers.
run:
ifeq ($(server), frontend)
	echo not implemented yes
else ifeq ($(server), backend)
	$(backend) && $(CMD) python3 manage.py runserver
endif
