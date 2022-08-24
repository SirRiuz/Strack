

FROM python:3.9

WORKDIR /app

COPY . .

RUN dir
RUN pip install --no-cache-dir --upgrade -r requirements.txt




CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "80"]




