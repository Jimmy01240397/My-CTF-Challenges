FROM debian:latest
RUN apt-get update && apt-get -y upgrade 
RUN apt-get install -y lsb-release curl wget iproute2 iputils-ping mtr dnsutils python3 python3-pip
COPY chal /app
WORKDIR /app
RUN echo 'python3 .' > start.sh
CMD ["bash", "start.sh"]

