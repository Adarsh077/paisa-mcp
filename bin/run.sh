docker build -t paisa-mcp .
docker rm -f paisa-mcp
docker run --name paisa-mcp --add-host=host.docker.internal:host-gateway --env-file .env -p 8000:8000 -d paisa-mcp