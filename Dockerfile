FROM debian:buster

RUN apt update && apt upgrade -y \
    curl python python-pip python-dev python -V git wget vim zlib1g-dev libtiff-dev libfreetype6 libfreetype6-dev libwebp-dev libopenjp2-7-dev libopenjp2-7-dev python-numpy libopenjp2-7 i2c-tools \
&& pip install RPi.GPIO paho-mqtt datetime pillow

RUN git clone https://github.com/RPi-Distro/RTIMULib/ RTIMU

WORKDIR ./RTIMU/Linux/python

RUN python setup.py build \
&& python setup.py install \
&& pip install sense-hat

WORKDIR /root

RUN git clone --depth 1 https://github.com/akihiro0000/senseHat.git

WORKDIR /root/senseHat
