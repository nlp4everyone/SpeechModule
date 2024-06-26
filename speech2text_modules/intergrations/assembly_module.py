import assemblyai as aai
from config import transcript_params
import os

class AssemblyS2TModule():
    def __init__(self, api_key : str = transcript_params.ASSEMBLYAI_KEY):
        """Initialize Assembly Speech to text Module with specific params."""
        # Validate
        assert api_key is not None
        # Set API Key
        aai.settings.api_key = api_key

        # Other setting
        self._transcriber = aai.Transcriber()
        self._config = aai.TranscriptionConfig(speaker_labels=True)

    def transcribe(self, audio_path: str) -> str:
        if not os.path.exists(audio_path):
            raise Exception("File is not existed!")
        # Get value
        transcript = self._transcriber.transcribe(audio_path)
        return transcript.text


