# Set the base image to Ubuntu
FROM ubuntu:xenial

# Set the file maintainer
MAINTAINER Hendrik Buchwald

# Install dependencies
RUN apt-get update  && \
    apt-get -y install git curl lighttpd php-cgi php-cli php-pgsql php-mysql php-dom php-zip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Enable PHP in Lighttpd
RUN ln -s /etc/lighttpd/conf-available/10-fastcgi.conf /etc/lighttpd/conf-enabled/ && \
    ln -s /etc/lighttpd/conf-available/15-fastcgi-php.conf /etc/lighttpd/conf-enabled/

# Create required directory
RUN mkdir /var/run/lighttpd/ &&\
    chown www-data:www-data /var/run/lighttpd/

# Copy a configuration file from the current directory
ADD lighttpd.conf /etc/lighttpd/

# Install shadowd_ui
WORKDIR /var
RUN git clone https://github.com/zecure/shadowd_ui.git
WORKDIR /var/shadowd_ui
ADD parameters.yml.dist app/config/parameters.yml

ENV SYMFONY_ENV prod

RUN \
    php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \
    php -r "if (!hash_file('SHA384', 'composer-setup.php') === '93b54496392c062774670ac18b134c3b3a95e5a5e5c8f1a9f115f203b75bf9a129d5daa8ba6a13e2cc8a1da0806388a8') { unlink('composer-setup.php'); exit(1); }" && \
    php composer-setup.php && \
    php -r "unlink('composer-setup.php');" && \
    php composer.phar -n install --no-dev --no-scripts && \
    rm composer.phar && \
    chown -R www-data:www-data app/cache app/logs

# Port to expose
EXPOSE 80

# Set the default command to run when starting the container
CMD ["/usr/sbin/lighttpd", "-f", "/etc/lighttpd/lighttpd.conf", "-D"]

# Set custom entrypoint
COPY ./docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]
