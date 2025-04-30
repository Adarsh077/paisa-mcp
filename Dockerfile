FROM python:3.13.3-alpine

WORKDIR /app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

# CMD ["mcp", "dev", "server.py"]
CMD ["uv", "run", "server.py", "--server_type=sse"]
