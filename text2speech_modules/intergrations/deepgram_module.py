from deepgram import DeepgramClient, SpeakOptions
from config import transcript_params
import os

class DeepGramT2SModule():
    def __init__(self, model: str = "aura-asteria-en", container :str = "wav"):
        """Initialize DeepGram Text to speech Module with specific params."""
        # Create a Deepgram client.
        self._client = DeepgramClient(api_key=transcript_params.DEEPGRAM_KEY)

        #Configure the options
        self.__options = SpeakOptions(
            model = model,
            encoding="linear16",
            container = container
        )

        # Initialize path
        os.makedirs(transcript_params.audio_directory, exist_ok=True)

    def generate(self, transcript: str, file_name :str = "sample.mp3"):
        # Define speak options
        SPEAK_OPTIONS = {"text": transcript}
        # Saved path
        saved_path = os.path.join(transcript_params.audio_directory, file_name)

        # Call the save method on the speak property
        self._client.speak.v("1").save(saved_path, SPEAK_OPTIONS, self.__options)
