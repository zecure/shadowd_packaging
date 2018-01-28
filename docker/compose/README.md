## Usage

Set a database password in `.env`.

    docker-compose up -d

Wait until the shadowd_ui container is started (15-30 seconds).

    docker-compose exec web php app/console swd:user:create
