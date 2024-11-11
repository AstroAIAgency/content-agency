from agency_swarm.tools import BaseTool
from pydantic import Field
import os

class ScriptEditorTool(BaseTool):
    """
    A tool for writing and editing scripts in Markdown format.
    """
    script_content: str = Field(..., description="The content of the script in Markdown format.")
    file_path: str = Field(..., description="The file path where the script will be saved.")

    def run(self):
        """
        Writes the script content to a specified file path.
        """
        with open(self.file_path, 'w') as file:
            file.write(self.script_content)
        return f"Script saved to {self.file_path}"

if __name__ == "__main__":
    tool = ScriptEditorTool(script_content="# Sample Script\nThis is a sample script.", file_path="sample_script.md")
    print(tool.run())
