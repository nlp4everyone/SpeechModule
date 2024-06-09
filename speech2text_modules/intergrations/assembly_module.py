import assemblyai as aai
from config import transcript_params

class AssemblyTranscriptModule():
    def __init__(self, api_key : str = transcript_params.ASSEMBLYAI_KEY):
        if not isinstance(api_key,str):
            raise Exception("API Key must be string")

        # Set API Key
        aai.settings.api_key = api_key

        # Other setting
        self._transcriber = aai.Transcriber()
        self._config = aai.TranscriptionConfig(speaker_labels=True)

    def transcribe(self, audio_path: str) -> str:
        # Get value
        transcript = self._transcriber.transcribe(audio_path)
        return transcript.text


