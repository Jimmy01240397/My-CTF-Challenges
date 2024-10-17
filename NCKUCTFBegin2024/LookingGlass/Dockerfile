from python:bookworm

RUN apt-get clean && apt-get update && apt-get install -y iputils-ping traceroute iproute2
RUN useradd -s /bin/bash -m app && \
    mkdir /app && \
    chown app:app /app

USER app
WORKDIR /app

COPY src/requirements.txt .

RUN pip install -r requirements.txt

COPY --chown=app:app src/ /app

ENTRYPOINT ["python", "."]



