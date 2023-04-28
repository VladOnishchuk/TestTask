###########
# BUILDER #
###########

# pull official base image
FROM python:3.9.6-alpine as builder

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV SERVICE_NAME=docker_user

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev gettext curl


# install dependencies
COPY ./requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/app/wheels -r requirements.txt


#########
# FINAL #
#########

# pull official base image
FROM python:3.9.6-alpine

# create directory for the app user
RUN mkdir -p /home/app

# create the appropriate directories
ENV HOME=/home/app
ENV APP_HOME=/home/app/web
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

# install dependencies
RUN apk update && apk add libpq gettext-dev
COPY --from=builder /usr/src/app/wheels /wheels
COPY --from=builder /usr/src/app/requirements.txt .
RUN pip install --no-cache /wheels/*

# copy entrypoint
COPY ./entrypoint .
RUN sed -i 's/\r$//g' entrypoint
RUN chmod +x entrypoint

COPY ./start.dev .
RUN sed -i 's/\r$//g' start.dev
RUN ["chmod", "+x", "start.dev"]

COPY ./start-celery-worker .
RUN sed -i 's/\r$//g' start-celery-worker
RUN ["chmod", "+x", "start-celery-worker"]

# copy project
COPY . $APP_HOME

# create the additional directories
RUN mkdir -p $APP_HOME/staticfiles
RUN mkdir -p $APP_HOME/media
RUN mkdir -p $APP_HOME/task_results

# run entrypoint
ENTRYPOINT ["sh", "/home/app/web/entrypoint"]