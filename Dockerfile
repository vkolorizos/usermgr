FROM python:3.9-slim-buster

RUN apt-get update && apt-get install -y \
    binutils \
    libproj-dev \
    git


RUN rm -rf /var/lib/apt/lists/*

RUN mkdir /config
COPY config/app/requirements.txt config/requirements.txt
COPY config/app/on-container-start.sh config/on-container-start.sh

RUN pip3 install --no-cache-dir -r config/requirements.txt
RUN chmod -x config/on-container-start.sh

EXPOSE 9000

RUN mkdir /app
WORKDIR /app
ADD app /app/
RUN mkdir -p media

CMD ["sh", "/config/on-container-start.sh"]