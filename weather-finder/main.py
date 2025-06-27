from mcp.server.fastmcp import FastMCP


mcp = FastMCP("WeatherFinder")


@mcp.tool()
def get_weather(city: str):
    """Provide proper weather information for given city with temperature , humidity, ..etc"""
    return f"The weather in {city} is sunny with a temperature of 20 degrees Celsius and a humidity of 50%."


# Resource implementation
@mcp.resource("weather://{location}")
def weather_resource(location: str) -> str:
    """Provide weather data as a resource."""
    return f"Weather data for {location}: Sunny, 72°F"


# Prompt implementation
@mcp.prompt()
def weather_report(location: str) -> str:
    """Create a weather report prompt."""
    return f"""You are a weather reporter. Weather report for {location}?"""


if __name__ == "__main__":
    mcp.run(transport="sse", port=3000)
