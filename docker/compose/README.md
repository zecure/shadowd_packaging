### Requirements

Install [Docker CE](https://docs.docker.com/install/), and [Docker Compose](https://docs.docker.com/compose/install/).

### Setup

You install and control Shadow Daemon through `shadowdctl`, a simple docker-compose wrapper.

    sudo ./shadowdctl up -d

Wait until the shadowd_ui container is started (15-30 seconds) and add a user account.

    sudo ./shadowdctl exec web php app/console swd:register --admin --name=arg (--email=arg)

You need this user account to log in to the web interface.
The e-mail address is optional.

For more information about other commands check out the [Docker Compose manual](https://docs.docker.com/compose/).

### Configuration

You can change the paths of the database and the database password in the file `.env`.
