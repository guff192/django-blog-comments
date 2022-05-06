build:
	docker-compose build api
run:
	docker-compose up -d api
migrate:
	docker-compose exec api python3 manage.py migrate
createdb:
	docker-compose exec db createdb -U postgres blog
