FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /tmp/requirements.txt
COPY requirements_prod.txt /tmp/requirements_dev.txt
RUN python -m pip install -r /tmp/requirements_dev.txt
COPY . /code/