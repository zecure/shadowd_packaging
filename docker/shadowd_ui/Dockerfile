# Set the base image to Ubuntu
FROM ubuntu

# Set the file maintainer
MAINTAINER Hendrik Buchwald

# Update the system
RUN apt-get update

# Install dependencies
RUN apt-get -y install git curl lighttpd php5-cgi php5-cli php5-pgsql php5-mysql

# Enable PHP in Lighttpd
RUN ln -s /etc/lighttpd/conf-available/10-fastcgi.conf /etc/lighttpd/conf-enabled/ &&\
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
ADD parameters.yml.dist app/config/
RUN curl -s https://getcomposer.org/installer | php &&\
    php composer.phar -n install &&\
    chown -R www-data:www-data app/cache app/logs

# Port to expose
EXPOSE 80

# Install start script
ADD start_server.sh /usr/sbin/
RUN chmod 755 /usr/sbin/start_server.sh

# Set the default command to run when starting the container
CMD ["/usr/sbin/start_server.sh"]
