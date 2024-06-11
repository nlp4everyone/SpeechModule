from groq import Groq
from config import transcript_params

class GroqS2TModule():
    def __init__(self, api_key : str = transcript_params.GROQ_KEY):
        """Initialize Groq Speech to text Module with specific params."""
        # Validate
        assert api_key is not None

        # Set API Key
        self._client = Groq(api_key = api_key)

    def transcribe(self, audio_path: str) -> str:
        with open(audio_path, "rb") as file:
            transcription = self._client.audio.transcriptions.create(
                file = (audio_path, file.read()),
                model="whisper-large-v3",
            )
        return transcription.text


