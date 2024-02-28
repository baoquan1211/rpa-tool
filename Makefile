POSTGRES_USER=root
POSTGRES_PASSWORD=2112

redis:
	docker run -d -p 6379:6379 redis
postgres:
	docker run --name postgres -p 5432:5432 -e POSTGRES_USER=$(POSTGRES_USER) -e POSTGRES_PASSWORD=$(POSTGRES_PASSWORD) -d postgres:alpine
createdb:
	docker exec -it postgres createdb -U $(POSTGRES_USER) -O $(POSTGRES_USER) rpa-scheduler
schedule:
	celery -A schedulers worker --loglevel=INFO
.PHONY: redis, schedule, createdb, postgres