from gtts import gTTS
from config import transcript_params
import os

class gTTSModule():
    def __init__(self, lang: str = "en"):
        """Initialize gTTS Text to speech Module with specific params."""

        # Define lang
        self._lang = lang

        # Initialize path
        os.makedirs(transcript_params.audio_directory, exist_ok=True)

    def generate(self,text :str,file_name: str = "sample.mp3"):
        # List of audio format
        audio_extensions = ["mp3","wav"]
        audio_extensions = [f".{ext}" for ext in audio_extensions]

        # Validate
        assert isinstance(text,str), "Text must be string"
        # Check format
        extension = os.path.splitext(file_name)[-1]
        if extension not in audio_extensions:
            raise Exception("Wrong audio path. Must be end at .mp3 or .wav format!")

        # Initialize object
        tts = gTTS(text = text, lang = self._lang)

        # Saved path
        saved_path = os.path.join(transcript_params.audio_directory,file_name)
        # Save the audio as predefined path
        tts.save(saved_path)