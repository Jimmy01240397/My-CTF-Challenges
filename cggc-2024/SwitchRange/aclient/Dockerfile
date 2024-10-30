FROM debian:latest
RUN apt-get update && apt-get -y upgrade 
RUN apt-get install -y lsb-release curl wget iputils-ping mtr dnsutils python3 python3-pip
RUN useradd -s /bin/bash -m app
WORKDIR /app
RUN chown app:app .
USER app
COPY chal/requirements.txt .
RUN pip3 install -r requirements.txt --break-system-packages
COPY chal/__main__.py .
COPY chal/templates .
RUN echo 'python3 .' > start.sh
CMD ['bash', 'start.sh']

