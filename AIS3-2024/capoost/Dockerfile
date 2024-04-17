FROM golang:1.19 as builder

RUN apt install make

COPY . /src
WORKDIR /src
RUN make && make readflag


FROM debian:latest as release

COPY --from=builder /src/bin /app
COPY template /app/template
COPY fl4g1337 /fl4g1337

RUN mv /app/readflag /readflag && \
    chown root:root /readflag && \
    chmod 4555 /readflag && \
    chown root:root /fl4g1337 && \
    chmod 400 /fl4g1337 && \
    useradd -m -s /bin/bash app && \
    chown app:app /app

USER app
WORKDIR /app

RUN touch .env

ENTRYPOINT ["./capoost"]
