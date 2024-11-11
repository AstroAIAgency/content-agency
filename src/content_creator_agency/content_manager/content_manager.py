from agency_swarm import Agent
from .tools.script_editor import ScriptEditorTool

class ContentManager(Agent):
    def __init__(self):
        super().__init__(
            name="Content Manager",
            description="Generates content ideas and writes scripts.",
            instructions="./instructions.md",
            tools=[ScriptEditorTool],
            temperature=0.7,
            max_prompt_tokens=3000,
        )
