FROM postgres:9.6

# Install dependencies
RUN apt-get update  && \
    apt-get -y install git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /tmp
RUN \
    git clone https://github.com/zecure/shadowd.git && \
    cp shadowd/misc/databases/pgsql_layout.sql /docker-entrypoint-initdb.d

ENV POSTGRES_USER shadowd
