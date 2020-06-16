FROM ubuntu:18.04

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       postgresql-client \
    && rm -rf /var/lib/apt/lists/* 

RUN apt-get update
RUN apt-get install -y build-essential python3 python3-dev python3-pip python3-venv libpq-dev

ADD . /app/
WORKDIR /app

RUN python3 -m pip install pip --upgrade \ 
    && python3 -m pip install wheel \
    && python3 -m pip install -U setuptools

RUN python3 -m pip install -r /app/requirements.txt
RUN apt-get update
RUN apt-get install -y ffmpeg && apt-get install -y libsndfile-dev
RUN apt-get update && apt-get install -y wget
ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

ENTRYPOINT ["/app/start"]
