FROM ubuntu:22.04

# Set the environment variable
ENV DJANGO_DEBUG=$DJANGO_DEBUG
ENV DJANGO_SUPERUSER_EMAIL=$DJANGO_SUPERUSER_EMAIL
ENV DJANGO_SUPERUSER_PASSWORD=$DJANGO_SUPERUSER_PASSWORD

ENV DATABASE_NAME=$DATABASE_NAME
ENV DATABASE_USER=$DATABASE_USER
ENV DATABASE_PASSWORD=$DATABASE_PASSWORD
ENV DATABASE_HOST=$DATABASE_HOST
ENV DATABASE_PORT=$DATABASE_PORT

ENV SERVER_DOMAIN_NAME=$SERVER_DOMAIN_NAME

ENV ENV=$ENV

RUN echo deb http://be.archive.ubuntu.com/ubuntu/ focal main restricted universe multiverse >> /etc/apt/sources.list
RUN apt-get -y update && \
    apt-get -y install wget sudo netcat redis vim python3.8 python3-pip && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /backend

RUN wget -O /sbin/zinit https://github.com/threefoldtech/zinit/releases/download/v0.2.5/zinit && \
  chmod +x /sbin/zinit && pip install poetry && poetry --version

RUN mkdir -p /etc/zinit/

COPY ./backend /backend
COPY ./docker/scripts/backend/zinit /etc/zinit
COPY ./docker/scripts/backend/*.sh /backend/scripts/
COPY ./config /config/

RUN chmod +x /backend/scripts/*.sh

EXPOSE 8000
ENTRYPOINT  ["zinit", "init"]