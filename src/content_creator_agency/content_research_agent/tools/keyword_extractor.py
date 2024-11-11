from agency_swarm.tools import BaseTool
from pydantic import Field

try:
    import nltk
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize

    # Download required NLTK data
    nltk.download('punkt', quiet=True)
    nltk.download('stopwords', quiet=True)
    nltk.download('punkt_tab', quiet=True)  # Add this line to download punkt_tab
except ImportError:
    print("NLTK is not installed. Please run 'pip install nltk' and try again.")
    raise

class KeywordExtractorTool(BaseTool):
    """
    A tool for extracting keywords from text using NLTK.
    """
    text: str = Field(..., description="The text from which to extract keywords.")

    def run(self):
        """
        Extracts keywords from the provided text.
        """
        try:
            stop_words = set(stopwords.words('english'))
            word_tokens = word_tokenize(self.text)
            keywords = [word for word in word_tokens if word.isalnum() and word not in stop_words]
            return keywords
        except LookupError as e:
            print(f"Error: {e}")
            print("Attempting to download missing NLTK data...")
            nltk.download('punkt_tab')
            # Retry after downloading
            stop_words = set(stopwords.words('english'))
            word_tokens = word_tokenize(self.text)
            keywords = [word for word in word_tokens if word.isalnum() and word not in stop_words]
            return keywords

if __name__ == "__main__":
    # Ensure all necessary NLTK data is downloaded
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('punkt_tab')  # Add this line to download punkt_tab
    
    tool = KeywordExtractorTool(text="AI is transforming the world with new trends emerging daily.")
    print(tool.run())
