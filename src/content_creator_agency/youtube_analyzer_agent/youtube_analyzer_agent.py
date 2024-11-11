from agency_swarm import Agent
from .tools.youtube_analyzer import YouTubeAnalyzerTool

class YouTubeAnalyzerAgent(Agent):
    def __init__(self):
        super().__init__(
            name="YouTube Analyzer Agent",
            description="Analyzes competitors' YouTube channels to identify content gaps and top-performing topics.",
            instructions="./instructions.md",
            tools=[YouTubeAnalyzerTool],
            temperature=0.5,
            max_prompt_tokens=3000,
        )
