# Set the base image to Ubuntu
FROM ubuntu

# Set the file maintainer
MAINTAINER Hendrik Buchwald

# Update the system
RUN apt-get update

# Install shadowd
RUN apt-get -y install software-properties-common &&\
    add-apt-repository -y ppa:zit-hb/shadowd &&\
    apt-get update &&\
    apt-get -y install shadowd

# Copy a configuration file from the current directory
ADD shadowd.ini /etc/shadowd/

# Port to expose
EXPOSE 9115

# Set the default command to run when starting the container
CMD ["/usr/bin/shadowd", "-c", "/etc/shadowd/shadowd.ini", \
     "-U", "shadowd", "-G", "shadowd"]
