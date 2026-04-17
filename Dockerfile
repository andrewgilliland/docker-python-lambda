FROM public.ecr.aws/lambda/python:3.14

COPY pyproject.toml ${LAMBDA_TASK_ROOT}
RUN pip install fastapi mangum uvicorn --target ${LAMBDA_TASK_ROOT}

COPY main.py events.json ${LAMBDA_TASK_ROOT}

CMD ["main.handler"]
