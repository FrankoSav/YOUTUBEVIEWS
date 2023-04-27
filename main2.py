#!/bin/bash

sudo apt-get install wmctrl xdotool
clear

echo "Youtube Views"
sleep 5
clear

urls=(
    "https://www.youtube.com/watch?v=MuYC7MyThDY"
    "https://www.youtube.com/watch?v=MuYC7MyThDY"
    "https://www.youtube.com/watch?v=MuYC7MyThDY"
)

for url in "${urls[@]}"
do
    open "$url"
    sleep 1
    xdotool key space
    sleep 5
    wmctrl -c "Mozilla Firefox"
done
