# Set the base image to Ubuntu
FROM ubuntu:18:04

# Set the file maintainer
MAINTAINER Hendrik Buchwald

# Environment
ENV SYMFONY_ENV prod

# Port to expose
EXPOSE 80

# Install dependencies
RUN apt-get update  && \
    apt-get -y install git curl lighttpd php-cgi php-cli php-pgsql php-mysql php-dom php-zip composer && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Enable PHP in Lighttpd
RUN ln -s /etc/lighttpd/conf-available/10-fastcgi.conf /etc/lighttpd/conf-enabled/ && \
    ln -s /etc/lighttpd/conf-available/15-fastcgi-php.conf /etc/lighttpd/conf-enabled/

# Create required directory
RUN mkdir /var/run/lighttpd/ &&\
    chown www-data:www-data /var/run/lighttpd/

# Copy a configuration file from the current directory
ADD files/lighttpd.conf /etc/lighttpd/

# Set the default command to run when starting the container
CMD ["/usr/sbin/lighttpd", "-f", "/etc/lighttpd/lighttpd.conf", "-D"]

# Set custom entrypoint
COPY files/docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]

# Install shadowd_ui
COPY source /var/shadowd_ui
WORKDIR /var/shadowd_ui
COPY files/parameters.yml.dist app/config/parameters.yml
RUN composer -n install --no-dev --no-scripts && \
    chown -R www-data:www-data app/cache app/logs
