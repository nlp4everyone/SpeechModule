from groq import Groq
from config import transcript_params

class GroqTranscriptModule():
    def __init__(self, api_key : str = transcript_params.GROQ_KEY):
        if not isinstance(api_key,str):
            raise Exception("API Key must be string")

        # Set API Key
        self._client = Groq(api_key = api_key)

    def transcribe(self, audio_path: str) -> str:
        with open(audio_path, "rb") as file:
            transcription = self._client.audio.transcriptions.create(
                file = (audio_path, file.read()),
                model="whisper-large-v3",
            )
        return transcription.text


