#!/bin/sh
sed -i "s/ThisTokenIsNotSoSecretChangeIt/$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)/g" /var/shadowd_ui/app/config/parameters.yml
/usr/sbin/lighttpd -f /etc/lighttpd/lighttpd.conf -D
