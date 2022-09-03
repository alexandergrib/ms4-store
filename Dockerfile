###########
# BUILDER #
###########

# pull official base image
FROM python:3.9.2-alpine as builder

# set work directory
WORKDIR /usr/src/ms4_shop

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# lint
RUN pip install --upgrade pip
RUN pip install flake8
COPY . .
#RUN flake8 --ignore=E501,F401 .

# install dependencies
COPY ./requirements.txt .
RUN pip install --upgrade pip
# install psycopg2

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add jpeg-dev zlib-dev libjpeg \
    && apk add python3-dev py3-setuptools \
    && apk add tiff-dev jpeg-dev openjpeg-dev zlib-dev freetype-dev lcms2-dev \
    libwebp-dev tcl-dev tk-dev harfbuzz-dev fribidi-dev libimagequant-dev \
    libxcb-dev libpng-dev \
    && apk del build-deps






RUN pip wheel --no-cache-dir --no-deps --wheel-dir /usr/src/ms4_shop/wheels -r requirements.txt




#########
# FINAL #
#########

# pull official base image
FROM python:3.9.2-alpine

# create directory for the app user
RUN mkdir -p /home/


# create the app user
RUN addgroup -S webuser && adduser -S webuser -G webuser

# create the appropriate directories
ENV HOME=/home/ms4_shop
ENV APP_HOME=/home/ms4_shop/web
RUN mkdir -p $APP_HOME
RUN mkdir $APP_HOME/staticfiles
RUN mkdir $APP_HOME/media
WORKDIR $APP_HOME

# install dependencies
RUN apk update && apk add libpq
COPY --from=builder /usr/src/ms4_shop/wheels /wheels
COPY --from=builder /usr/src/ms4_shop/requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache /wheels/*

# copy entrypoint-prod.sh
#COPY --chmod=0755 ./entrypoint.prod.sh $APP_HOME

# copy project
COPY . $APP_HOME
COPY ./media $APP_HOME/media
COPY ./static $APP_HOME/staticfiles

# chown all the files to the app user
RUN chown -R webuser:webuser $APP_HOME

# change to the app user
USER webuser

# run entrypoint.prod.sh
RUN ["chmod", "+x", "/home/ms4_shop/web/entrypoint.sh"]


RUN python manage.py collectstatic --no-input --clear
RUN python manage.py makemigrations
RUN python manage.py migrate