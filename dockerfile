FROM python:3.9-alpine
RUN apk --update add --virtual build-dependencies build-base libffi-dev postgresql-dev linux-headers bash cargo
RUN apk --update add --virtual git-dependencies git-lfs
RUN mkdir /code
WORKDIR /code
ADD . /code
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
