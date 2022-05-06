#syntax=docker/dockerfile:1
FROM python:3.10-slim
WORKDIR /blog

# install requirements
COPY . .
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt --no-cache-dir

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
