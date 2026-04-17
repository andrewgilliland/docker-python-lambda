def handler(event, context):
    print("Hello from docker-python-lambda!")
    return {
        "statusCode": 200,
        "body": "Hello from docker-python-lambda!"
    }


if __name__ == "__main__":
    handler({}, None)
