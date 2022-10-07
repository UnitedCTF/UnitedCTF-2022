FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y socat && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY challenge /challenge
COPY run.sh flag /

RUN chmod 444 /flag && \
    chmod 500 /run.sh && \
    DIRNAME=$(mktemp -u XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX) && \
    mkdir /$DIRNAME && \
    mv /flag /$DIRNAME && \
    chown -R root:root /challenge /$DIRNAME

EXPOSE 1337

ENTRYPOINT ["/run.sh"]
