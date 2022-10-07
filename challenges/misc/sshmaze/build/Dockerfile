FROM alpine

RUN apk add --no-cache openssh-server openssh-client bind-tools
RUN ssh-keygen -A

RUN addgroup -g 1000 maze
RUN adduser -D -u 1000 cell -G maze

# Unlock the user
RUN sed -ri 's/cell:!/cell:\*/g' /etc/shadow

# Hide the contents of /tmp between users
RUN chmod o-r /tmp

COPY --chown=root:root /root /

# Hide the entrypoint
RUN chmod 700 /entrypoint.sh
ENTRYPOINT [ "/entrypoint.sh" ]
