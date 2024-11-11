from agency_swarm.tools import BaseTool
from pydantic import Field
from pytrends.request import TrendReq

class KeywordAnalyzerTool(BaseTool):
    """
    A tool for analyzing keywords using Pytrends.
    """
    keywords: list = Field(..., description="A list of keywords to analyze.")

    def run(self):
        """
        Analyzes the provided keywords using Pytrends.
        """
        pytrends = TrendReq()
        pytrends.build_payload(self.keywords, cat=0, timeframe='today 12-m', geo='', gprop='')
        trends = pytrends.interest_over_time()
        return trends.to_dict()

if __name__ == "__main__":
    tool = KeywordAnalyzerTool(keywords=["AI", "machine learning"])
    print(tool.run())
