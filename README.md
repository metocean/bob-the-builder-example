# bob-the-builder-example
An exmaple project the is setup to use bob-the-builder build server

The demo code does:  
client > POST > http://server:8080/db/john
client < GET < http://server:8080/db/john

## docker-compose.yml
```
version: '2'

services:

  server:
    build: ./server/

  client:
    build: ./client/
    depends_on:
      - server
    links:
      - server
```
## bob-the-builder.yml
```
docker_compose:
    file: docker-compose.yml
    test_service: client
    services_to_push:
        server: metocean/bob-example-server
        client: metocean/bob-example-client

notification_emails:
    - [some-one-at]@gmail.com
```
* docker_compose:  
..* file: points to the docker compose file to build (default: docker-compose.yml')
..* test_service: points to the docker compose service to run / test. If this docker exits with a non-zero the build fails.
..* services_to_push: tell bob what services to push to docker hub.
...* server: metocean/bob-example-server e.g. service "server" is push to docker hub as "metocean/bob-example-server"
