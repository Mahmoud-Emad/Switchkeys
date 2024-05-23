#!/bin/sh

set -e

# Function to wait for PostgreSQL
wait_for_postgres() {
    echo "Waiting for PostgreSQL to be running on: $DATABASE_HOST"
    while ! nc -z $DATABASE_HOST $DATABASE_PORT; do
        sleep 0.1
    done
    echo "PostgreSQL started"
}

# Function to run common Django commands
run_django_commands() {
    cd backend
    poetry run python3 manage.py flush --no-input
    echo "Running the migration"
    poetry run python3 manage.py makemigrations
    echo "Running the migrate"
    poetry run python3 manage.py migrate
}

# Function to create superuser if not exists
create_superuser_if_not_exists() {
    echo "Checking if superuser exists..."
    poetry run python3 manage.py create_superuser
}

# Main script execution
if [ "$ENV" = "production" ]; then
    echo "Running in production mode."
    wait_for_postgres
    run_django_commands
    create_superuser_if_not_exists
else
    echo "Running in development mode."
    run_django_commands
    echo "Creating a superuser email: $DJANGO_SUPERUSER_EMAIL"
    poetry run python3 manage.py createsuperuser --noinput
fi

# Continue with the provided command or entry point
exec "$@"
