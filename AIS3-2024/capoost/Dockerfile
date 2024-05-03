FROM golang:1.19 as builder

RUN apt install make

COPY src /src
WORKDIR /src
RUN make clean && make && make readflag


FROM debian:latest as release

LABEL maintainer="Chumy"

COPY --from=builder /src/bin /app
COPY src/template /app/template
COPY src/fl4g1337 /fl4g1337

RUN mv /app/readflag /readflag && \
    chown root:root /readflag && \
    chmod 4555 /readflag && \
    chown root:root /fl4g1337 && \
    chmod 400 /fl4g1337 && \
    mv /app/capoost /app/aebiaxxSJJpTWnkj && \
    useradd -m -s /bin/bash app && \
    chown -R app:app /app

USER app
WORKDIR /app

RUN touch .env

ENTRYPOINT ["./aebiaxxSJJpTWnkj"]
