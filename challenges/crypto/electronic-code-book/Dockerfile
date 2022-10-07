FROM python:3.9-slim-bullseye

RUN apt-get update && \
    apt-get install -y socat && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install pycryptodome

COPY src /app
COPY run.sh /

RUN chmod +x /run.sh

ENTRYPOINT ["/run.sh"]
