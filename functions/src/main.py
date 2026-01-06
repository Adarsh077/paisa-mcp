from mcp.server.fastmcp import FastMCP
from mangum import Mangum
from tools.transactions import transactions_mcp
from tools.tags import tags_mcp

mcp = FastMCP("paisa")

transactions_mcp.register(mcp=mcp)
tags_mcp.register(mcp=mcp)

mcp_app = mcp.sse_app()

async def strict_headers_middleware(scope, receive, send):
    """
    Middleware to sanitize headers for AWS Lambda.
    It removes ALL existing Host/Accept headers to prevent duplicates/conflicts,
    then injects the specific values FastMCP expects.
    """
    if scope["type"] == "http":
        original_headers = scope.get("headers", [])
        clean_headers = []
        
        # 1. Filter out ANY existing Host or Accept headers (case-insensitive)
        for key, value in original_headers:
            k_lower = key.lower()
            if k_lower == b"host" or k_lower == b"accept":
                continue
            clean_headers.append((key, value))
        
        # 2. Force 'Host' to 127.0.0.1 (Safest for local/default binding checks)
        clean_headers.append((b"host", b"127.0.0.1"))
        
        # 3. Force 'Accept' header for SSE endpoints
        if scope["path"].endswith("/sse"):
            clean_headers.append((b"accept", b"text/event-stream"))
            
        scope["headers"] = clean_headers

    await mcp_app(scope, receive, send)

handler = Mangum(strict_headers_middleware)
