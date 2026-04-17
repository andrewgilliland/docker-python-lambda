# docker-python-lambda

A FastAPI app deployed as an AWS Lambda function, containerized with Docker.

## Requirements

- [Docker](https://www.docker.com/)
- [uv](https://docs.astral.sh/uv/)

## Setup

```bash
uv sync
```

## Commands

| Command | Description |
|---|---|
| `make build` | Build the Docker image |
| `make run` | Run FastAPI locally with hot reload (no Docker) |
| `make serve` | Run FastAPI in Docker on `http://localhost:8000` |
| `make start` | Run the Lambda RIE in Docker on port 9000 |
| `make dev` | Run the Lambda RIE with local file mount (no rebuild needed) |
| `make invoke` | Send a test invocation to the Lambda RIE |

## Local Development

For the fastest feedback loop, run FastAPI directly:

```bash
make run
```

Then open:
- `http://localhost:8000/` — root endpoint
- `http://localhost:8000/health` — health check
- `http://localhost:8000/docs` — interactive Swagger UI

## Lambda Emulation

To simulate the Lambda environment locally:

```bash
make dev    # start container (mounts local main.py, no rebuild needed)
make invoke # invoke in a separate terminal
```
