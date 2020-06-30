#!/bin/bash

# Commands that you want to be run once connected can go here
cd /home/pi/iqube-web
/usr/bin/npm install
sudo /usr/bin/node /home/pi/iqube-web/app.js &

startx /home/pi/raspberry-pi-turnkey/xinitrc
