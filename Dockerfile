FROM python:alpine
LABEL maintainer="Puru Tuladhar <ptuladhar3@gmail.com>"

COPY install.sh .
RUN chmod +x install.sh
RUN ./install.sh

COPY scripts/send-email.py /send-email.py
