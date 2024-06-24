FROM python:3.10

LABEL maintainer="Chumy"

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -qy socat && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

COPY server /server

WORKDIR /server

RUN openssl req -x509 -new -nodes -days 3650 -newkey 2048 -keyout server.key -out server.crt -subj "/CN=$(hostname)"

ENTRYPOINT ["socat", "openssl-listen:8741,fork,reuseaddr,cert=server.crt,key=server.key,verify=0,openssl-min-proto-version=TLS1.3", "EXEC:'timeout 5 python3 server.py',stderr"]
