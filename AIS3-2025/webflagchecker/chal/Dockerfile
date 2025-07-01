FROM node:latest as builder

RUN apt update && apt install -y --no-install-recommends make git ca-certificates python3 && apt clean && rm -rf /var/lib/apt/lists/*

WORKDIR /build

RUN git clone https://github.com/emscripten-core/emsdk.git && \
    cd emsdk/ && \
    ./emsdk install latest && \
    ./emsdk activate latest

COPY src /build/src

WORKDIR /build/src

RUN bash -c "source /build/emsdk/emsdk_env.sh && make clean && make"

FROM nginx:latest as release

COPY --from=builder /build/src/bin /usr/share/nginx/html


