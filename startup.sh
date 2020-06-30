#!/bin/bash

# Commands that you want to be run once connected can go here
cd /home/pi/iqube-web
/usr/bin/npm install
sudo /usr/bin/node /home/pi/iqube-web/app.js &

# uncomment for testing:
#/home/pi/bin/test-turnkey.sh
#startx /home/pi/raspberry-pi-turnkey/xinitrc_ap

startx /home/pi/raspberry-pi-turnkey/xinitrc