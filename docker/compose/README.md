## Usage

Install Docker and Docker-Compose and execute `shadowdctl`, a Docker-Compose wrapper.

    sudo ./shadowdctl up -d

Wait until the shadowd_ui container is started (15-30 seconds) and add a user account.

    sudo ./shadowdctl exec web php app/console swd:user:create
