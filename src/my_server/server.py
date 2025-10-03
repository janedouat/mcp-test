# src/my_server/server.py
from mcp.server.fastmcp import FastMCP
from smithery.decorators import smithery
from pydantic import BaseModel, Field

class ConfigSchema(BaseModel):
    unit: str = Field("celsius", description="Temperature unit (celsius or fahrenheit)")

@smithery.server(config_schema=ConfigSchema)
def create_server(): 
    """Create and return a FastMCP server instance with session config."""
    
    server = FastMCP(name="Weather Server")

    @server.tool()
    def get_weather(city: str) -> str: 
        """Get weather for a city."""
    

        return f"Weather is great in {city}."

    return server