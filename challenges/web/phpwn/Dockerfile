FROM php:8.1-apache-buster

COPY challenge/ext /usr/src/php/ext

RUN apt-get update && \
    apt-get install -y libssl-dev && \
    docker-php-ext-configure phpwn --enable-phpwn CFLAGS="-O1 -fno-stack-protector" && \
    docker-php-ext-install phpwn

COPY challenge/app /var/www/html
COPY challenge/flag/flag /

RUN chmod 001 /flag