# Build

    docker build -t zecure/shadowd shadowd
    docker build -t zecure/shadowd_ui shadowd_ui
    docker build -t zecure/shadowd_database shadowd_database

# Download

    docker pull zecure/shadowd
    docker pull zecure/shadowd_ui
    docker pull zecure/shadowd_database

# Start

    docker run -d --name shadowd_database zecure/shadowd_database
    docker run -d -p 1337:80 --link shadowd_database:db zecure/shadowd_ui
    docker run -d -p 9115:9115 --link shadowd_database:db zecure/shadowd
