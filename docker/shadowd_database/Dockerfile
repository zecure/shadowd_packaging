# Set the base image to Ubuntu
FROM ubuntu

# Set the file maintainer
MAINTAINER Hendrik Buchwald

# Update the system
RUN apt-get update

# Install dependencies
RUN apt-get -y install git postgresql-9.3 postgresql-client-9.3

# Switch to privileged database role
USER postgres

# Add a user and database
RUN service postgresql start &&\
    createuser shadowd &&\
    createdb -O shadowd shadowd &&\
    service postgresql stop

# Allow remote connections
RUN echo "host all all 0.0.0.0/0 trust" > /etc/postgresql/9.3/main/pg_hba.conf &&\
    echo "listen_addresses='*'" >> /etc/postgresql/9.3/main/postgresql.conf

# Create database layout
WORKDIR /tmp
RUN git clone https://github.com/zecure/shadowd.git
RUN service postgresql start &&\
    psql -h127.0.0.1 -Ushadowd -w shadowd < shadowd/misc/databases/pgsql_layout.sql &&\
    psql -h127.0.0.1 -Ushadowd -w shadowd --command "INSERT INTO users (username, password, role, change_password) VALUES ('admin', '\$2y\$10\$YR0Q2pc5LZT0v9UXP5PXAOQX00v3WFEH9PAdHkMU47oeI0DvstvCe', 1, true);" &&\
    psql -h127.0.0.1 -Ushadowd -w shadowd --command "INSERT INTO settings (page_limit, sort_order, theme, open_filter, user_id, locale) VALUES (50, 0, 'united', false, 1, 'en');"

# Expose the PostgreSQL port
EXPOSE 5432

# Add VOLUMEs to allow backup of config, logs and databases
VOLUME ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]

# Set the default command to run when starting the container
CMD ["/usr/lib/postgresql/9.3/bin/postgres", "-D", "/var/lib/postgresql/9.3/main", \
     "-c", "config_file=/etc/postgresql/9.3/main/postgresql.conf"]
