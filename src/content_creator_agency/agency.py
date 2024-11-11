from agency_swarm import Agency
from .content_manager.content_manager import ContentManager
from .content_research_agent.content_research_agent import ContentResearchAgent
from .youtube_analyzer_agent.youtube_analyzer_agent import YouTubeAnalyzerAgent

content_manager = ContentManager()
content_research_agent = ContentResearchAgent()
youtube_analyzer_agent = YouTubeAnalyzerAgent()

agency = Agency(
    [
        content_manager,  # Content Manager is the entry point
        [content_manager, content_research_agent],  # Content Manager can communicate with Content Research Agent
        [content_manager, youtube_analyzer_agent],  # Content Manager can communicate with YouTube Analyzer Agent
    ],
    shared_instructions='agency_manifesto.md',
    temperature=0.5,
    max_prompt_tokens=3000
)

if __name__ == "__main__":
    agency.demo_gradio()
