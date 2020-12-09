FROM python:alpine
# MAINTAINER Puru Tuladhar <ptuladhar3@gmail.com>

COPY install.sh .
RUN chmod +x install.sh
RUN ./install.sh
