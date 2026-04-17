.PHONY: build start dev run serve invoke

build:
	docker build -t docker-python-lambda .

start:
	docker run -p 9000:8080 docker-python-lambda

dev:
	docker run -p 9000:8080 -v $(PWD)/main.py:/var/task/main.py docker-python-lambda

run:
	uv run uvicorn main:app --reload

serve:
	docker run -p 8000:8000 --entrypoint="" docker-python-lambda python -m uvicorn main:app --host 0.0.0.0 --port 8000

invoke:
	curl -X POST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
