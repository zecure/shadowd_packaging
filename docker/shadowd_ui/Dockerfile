# Build stage
FROM ubuntu:focal AS builder
WORKDIR /tmp
RUN \
    apt-get update  && \
    DEBIAN_FRONTEND=noninteractive apt-get -y install git php-cli php-pgsql php-mysql php-dom php-zip composer && \
    git clone https://github.com/zecure/shadowd_ui.git
WORKDIR /tmp/shadowd_ui
COPY files/parameters.yml.dist app/config/parameters.yml
RUN \
    composer -n install --no-dev --no-scripts && \
    chown -R www-data:www-data app/cache app/logs

###

FROM ubuntu:focal
MAINTAINER Hendrik Buchwald
ENV SYMFONY_ENV prod
EXPOSE 80
RUN \
    apt-get update  && \
    DEBIAN_FRONTEND=noninteractive apt-get -y install curl lighttpd php-cgi php-cli php-pgsql php-mysql php-dom php-zip && \
    ln -s /etc/lighttpd/conf-available/10-fastcgi.conf /etc/lighttpd/conf-enabled/ && \
    ln -s /etc/lighttpd/conf-available/15-fastcgi-php.conf /etc/lighttpd/conf-enabled/ && \
    mkdir /var/run/lighttpd/ &&\
    chown www-data:www-data /var/run/lighttpd/
ADD files/lighttpd.conf /etc/lighttpd/
CMD ["/usr/sbin/lighttpd", "-f", "/etc/lighttpd/lighttpd.conf", "-D"]
COPY files/docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
COPY --from=builder /tmp/shadowd_ui /var/shadowd_ui
WORKDIR /var/shadowd_ui

