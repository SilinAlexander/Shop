FROM python:3.8.5-alpine
MAINTAINER alexander

ENV HOME /usr/src/web
# set work directory
WORKDIR $HOME
ENV MY alexander
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV TZ Asia/Yekaterinburg
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND noninteractive

# install dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev openssl libffi-dev openssl-dev

# install Pillow dependencies
RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev harfbuzz-dev fribidi-dev

# install Ipython dependencies
RUN apk add build-base libzmq zeromq-dev


# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt $HOME/requirements.txt



RUN pip install -r $HOME/requirements.txt
# copy entrypoint.sh
COPY entrypoint.sh /entrypoint.sh
# copy project
COPY . /usr/src/web/
RUN chmod +x /entrypoint.sh