FROM debian:buster

RUN apt update && apt upgrade -y \
    curl python3 python3-pip python3-dev python3 -V git wget vim

RUN pip3 install RPi.GPIO paho-mqtt datetime

RUN apt install zlib1g-dev libtiff-dev libfreetype6 libfreetype6-dev libwebp-dev libopenjp2-7-dev libopenjp2-7-dev pyth
RUN pip3 install pillow

RUN pip3 install sense-hat

WORKDIR /root
