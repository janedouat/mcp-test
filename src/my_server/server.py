# src/my_server/server.py
from mcp.server.fastmcp import FastMCP
from smithery.decorators import smithery

@smithery.server()
def create_server(): 
    """Create and return a FastMCP server instance with session config."""
    
    server = FastMCP(name="Weather Server")

    @server.tool()
    def get_weather(city: str) -> str: 
        """Get weather for a city."""
    

        return f"Weather is great in {city}."

    return server