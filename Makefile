.PHONY: build start dev invoke

build:
	docker build -t docker-python-lambda .

start:
	docker run -p 9000:8080 docker-python-lambda

dev:
	docker run -p 9000:8080 -v $(PWD)/main.py:/var/task/main.py docker-python-lambda

invoke:
	curl -X POST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
