Ensure 
- [Docker](https://www.docker.com/get-started) installed on your machine.

1. clone repository
2. Provide Fivetran b64_api_key API Credentials to creds.toml
3. Build the Docker Image: from the Root directory of the project run: 
    ```
    docker build -t change-connectors . 
    ```
4. Run the Docker Container
```
docker run --rm -v "$(pwd)/creds.toml:/app/creds.toml" change-connectors
```

