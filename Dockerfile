FROM debian:buster

RUN apt update && apt upgrade -y \
    curl python python-pip python-dev python -V git wget vim

RUN pip install RPi.GPIO paho-mqtt datetime

RUN apt install zlib1g-dev libtiff-dev libfreetype6 libfreetype6-dev libwebp-dev libope
RUN pip install pillow

RUN git clone https://github.com/RPi-Distro/RTIMULib/ RTIMU

WORKDIR ./RTIMU/Linux/python

RUN python setup.py build
RUN python setup.py install

RUN apt install libopenjp2-7

RUN pip install sense-hat

WORKDIR /root
