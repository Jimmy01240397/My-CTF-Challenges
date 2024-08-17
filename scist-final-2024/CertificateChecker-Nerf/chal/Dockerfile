FROM python:3.11.9-bookworm

LABEL maintainer="Chumy"

RUN useradd -m app

USER app

WORKDIR /home/app

COPY requirements.txt .

RUN pip install -r requirements.txt --break-system-packages

COPY __main__.py .
COPY templates/ templates/

ENTRYPOINT ["python3", "."]


