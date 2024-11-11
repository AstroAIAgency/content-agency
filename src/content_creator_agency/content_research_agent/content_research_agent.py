from agency_swarm import Agent
from .tools.web_search import WebSearchTool
from .tools.keyword_extractor import KeywordExtractorTool
from .tools.keyword_analyzer import KeywordAnalyzerTool

class ContentResearchAgent(Agent):
    def __init__(self):
        super().__init__(
            name="Content Research Agent",
            description="Analyzes AI trends and compiles reports.",
            instructions="./instructions.md",
            tools=[WebSearchTool, KeywordExtractorTool, KeywordAnalyzerTool],
            temperature=0.5,
            max_prompt_tokens=3000,
        )
