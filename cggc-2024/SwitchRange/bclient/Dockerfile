FROM debian:latest
RUN apt-get update && apt-get -y upgrade 
RUN apt-get install -y lsb-release curl wget iputils-ping mtr dnsutils python3 python3-pip
RUN useradd -s /bin/bash -m app
COPY chal /app
WORKDIR /app
RUN chown app:app .
USER app
RUN echo 'python3 .' > start.sh
CMD ['bash', 'start.sh']

