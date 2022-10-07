FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y git zip unzip socat && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN useradd -m -s /bin/sh mrcrochet

ADD src /

RUN chmod +x /challenge.sh /run.sh

USER mrcrochet

EXPOSE 1337

ENTRYPOINT ["/run.sh"]
