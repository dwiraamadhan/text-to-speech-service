FROM python:3.12.2

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 8002

CMD ["uvicorn", "main:app", "--port", "8002"]