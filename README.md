Ensure 
- [Docker](https://www.docker.com/get-started) installed on your machine.

1. clone repository, then cd into the created ~/change-connectors folder
2. Input the generated Fivetran b64_api_key API Credentials  as outlined in this [API documentation](https://fivetran.com/docs/rest-api/getting-started) to env.toml
3. Build the Docker Image: from the Root directory of the project run: 
    ```
    docker build -t change-connectors . 
    ```
4. Run the Docker Container
```
docker run --rm -v "$(pwd)/creds.toml:/app/creds.toml" change-connectors
```

