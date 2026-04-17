# docker-python-lambda

A Python AWS Lambda function containerized with Docker.

## Usage

### Build the Docker image

```bash
make build
```

### Start the container locally

```bash
make start
```

### Invoke the Lambda function

In a separate terminal, after the container is running:

```bash
make invoke
```
