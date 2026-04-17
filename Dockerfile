FROM public.ecr.aws/lambda/python:3.14

COPY main.py ${LAMBDA_TASK_ROOT}

CMD ["main.handler"]
