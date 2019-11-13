#!/bin/sh

xset -dpms
xset s off
xset s noblank

unclutter &
exec chromium-browser http://0.0.0.0:8080 --window-size=480,320 --kiosk --incognito --noerrdialogs --fast --fast-start --disable-infobars --no-sandbox