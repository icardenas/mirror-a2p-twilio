SHELL := /bin/bash
.SUFFIXES:

up:
	docker-compose up

make bash:
	docker exec -it a2p_twilio_capp bash

runserver:
	python manage.py runserver 0.0.0.0:$(APP_PORT)

runworker:
	mrq-worker

create_user:
	python manage.py createsuperuser

migrate:
	python manage.py migrate

info:
	mrq-run --queue medium "tasks.twilio.GetInformation" '{"a": 1}'