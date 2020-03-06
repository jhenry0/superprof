run-rabbit:
	docker run -d --hostname rabbit --name rabbit --network webscraping rabbitmq:3
start-rabbit:
	docker start rabbit
build:
	docker build -t webscraping .
run:
	docker run -d --network webscraping --name celery webscraping celery -A tasks worker -Q save,superprof -c 10 --loglevel=info
logs:
	docker logs -f celery --tail 100
generaet:
	docker run --network webscraping webscraping python superprof.py