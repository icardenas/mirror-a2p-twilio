SHELL := /bin/bash
.SUFFIXES:


runserver:
	python manage.py runserver 0.0.0.0:$(APP_PORT)

createsuperuser:
	python manage.py createsuperuser