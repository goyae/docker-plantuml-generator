SHELL=/bin/sh

plant:
	docker-compose exec plantuml python plantuml.py

install:
	docker-compose down --volumes --remove-orphans
	docker-compose build
	docker-compose up -d

u:
	docker-compose up -d

d:
	docker-compose down

ps:
	docker-compose ps

c:
	docker-compose exec plantuml bash

r: d u c
