FROM debian:latest as builder

RUN apt update && apt install -y --no-install-recommends gcc make libc6-dev && apt clean && rm -rf /var/lib/apt/lists/*

COPY src /src

WORKDIR /src

RUN make clean && make

FROM nginx:latest as release

COPY --from=builder /src/bin/tcptunnel /usr/local/bin

COPY docker-entrypoint.d/* /docker-entrypoint.d/

RUN chmod +x /docker-entrypoint.d/*
RUN echo "AIS3{test}" > /usr/share/nginx/html/index.html

