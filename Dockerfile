FROM python:3.6-slim

ARG PASS="pass"
ENV USER="badger"

ENV WEEWX_DATABASE="/var/lib/weewx/weewx.sdb"
ENV DTS_PORT=24242

EXPOSE $PORT

#RUN useradd -m $USER
#RUN echo $USER:$PASS | chpasswd

# Packages
RUN apt-get update && apt-get -y install curl git
RUN pip install pipenv

# App
#USER badger
#WORKDIR /home/$USER/
WORKDIR /root/
RUN mkdir dts-server && cd dts-server
RUN curl -L https://api.github.com/repos/beasley-weather/dts-server/tarball | \
    tar xz --strip-components=1
#USER root
RUN pipenv install --system --skip-lock

# Cleanup
# UNCOMMENT BEFORE PROD
# RUN apt-get -y purge curl git && apt-get -y autoclean && apt-get -y autoremove

#USER badger
ENTRYPOINT python -m dts_server
