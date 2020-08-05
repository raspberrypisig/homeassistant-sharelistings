#!/usr/bin/env bash
echo "Copy files to right directory."
rsync -avu /home/pi/Developer/sharelistings /home/pi/homeassistant/share/hassio/addons/local
echo "Stopping existing addon."
ha addons stop local_share_listing
echo "Rebuilding addon."
ha addons rebuild local_share_listing
echo "Starting addon."
ha addons start local_share_listing
echo "Done."
