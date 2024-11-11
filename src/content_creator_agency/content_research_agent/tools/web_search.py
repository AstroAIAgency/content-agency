from agency_swarm.tools import BaseTool
from pydantic import Field
from tavily import TavilyClient
import os

class WebSearchTool(BaseTool):
    """
    A tool for searching the web using the Tavily API.
    """
    query: str = Field(..., description="The search query to execute.")

    def run(self):
        """
        Executes a web search using the Tavily API.
        """
        api_key = os.getenv("TAVILY_API_KEY")
        tavily_client = TavilyClient(api_key=api_key)
        response = tavily_client.search(self.query)
        return response

if __name__ == "__main__":
    tool = WebSearchTool(query="latest AI trends")
    print(tool.run())
