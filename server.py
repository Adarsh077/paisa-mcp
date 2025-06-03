from mcp.server.fastmcp import FastMCP
import argparse
from tools.transactions import transactions_mcp


mcp = FastMCP("paisa", host="0.0.0.0")

transactions_mcp.register(mcp=mcp)

if __name__ == "__main__":
    # Start the server
    print("🚀Starting server... ")

    # Debug Mode
    #  uv run mcp dev server.py

    # Production Mode
    # uv run server.py --server_type=sse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--server_type", type=str, default="sse", choices=["sse", "stdio"]
    )
    print("Server type: ", parser.parse_args().server_type)
    print("Launching on Port: ", 8000)
    print('Check "http://localhost:8000/sse" for the server status')

    args = parser.parse_args()
    mcp.run(args.server_type)
