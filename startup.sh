#!/bin/bash

# Commands that you want to be run once connected can go here
cd /home/pi/iqube-web
/usr/bin/npm install
/usr/bin/node /home/pi/iqube-web/index.js &

startx /home/pi/.xinitrc
