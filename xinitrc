#!/bin/sh

xset -dpms
xset s off
xset s noblank

unclutter &
exec chromium-browser http://0.0.0.0:80/time --window-size=480,320 --kiosk --incognito --noerrdialogs --fast --fast-start --disable-infobars --no-sandbox --disk-cache-dir=/dev/null --disk-cache-size=1