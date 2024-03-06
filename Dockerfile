FROM python:3.12

COPY . .

RUN pip install -r requirements.txt

WORKDIR src

CMD gunicorn main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000
