include .env.prod

build_prod_server:
	cp -r -u $(BINARIES_PATH) ./retina_help/
	docker-compose -f docker-compose.prod.yml up --build --remove-orphans -d
build_dev_server:
	docker-compose -f docker-compose.dev.yml up --build --remove-orphans -d

remove_prod_server:
	docker-compose -f docker-compose.prod.yml down -v
remove_dev_server:
	docker-compose -f docker-compose.dev.yml down -v

start_prod_server:
	docker-compose -f docker-compose.prod.yml up -d
start_dev_server:
	docker-compose -f docker-compose.dev.yml up -d

stop_prod_server:
	docker-compose -f docker-compose.prod.yml down
stop_dev_server:
	docker-compose -f docker-compose.dev.yml down

translations:
	django-admin makemessages -l de --ignore=venv/*

create_super_user:
	docker exec -ti retina_front-web-1 python manage.py createsuperuser