# Set the base image to Ubuntu
FROM ubuntu:xenial

# Set the file maintainer
MAINTAINER Hendrik Buchwald

# Copy shadowd package from the current directory
COPY shadowd_*.deb /tmp/

# Install shadowd
RUN apt-get update && \
    apt-get -y install libdbd-pgsql libdbd-mysql libboost-program-options1.58.0 libboost-regex1.58.0 libboost-system1.58.0 libboost-thread1.58.0 libcrypto++9v5 libdbi1 libssl1.0.0 && \
    dpkg -i /tmp/shadowd_*.deb && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/shadowd_*.deb

# Copy a configuration file from the current directory
COPY shadowd.ini /etc/shadowd/
RUN chown root:root /etc/shadowd/shadowd.ini && \
    chmod 640 /etc/shadowd/shadowd.ini

# Port to expose
EXPOSE 9115

# Set the default command to run when starting the container
CMD ["/usr/bin/shadowd", "-c", "/etc/shadowd/shadowd.ini", \
     "-U", "shadowd", "-G", "shadowd"]

# Set custom entrypoint
COPY ./docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]

ENV SHADOWD_ADDRESS 0.0.0.0
ENV SHADOWD_DB_HOST db
