import os.path

from deepgram import DeepgramClient , FileSource, PrerecordedOptions
from config import transcript_params

class DeepGramTranscriptModule():
    def __init__(self,
                 model_name :str = "nova-2",
                 api_key : str = transcript_params.DEEPGRAM_KEY):
        # Validate key
        if not isinstance(api_key,str):
            raise Exception("API Key must be string")

        # STEP 1 Create a Deepgram client using the API key
        self._client = DeepgramClient(api_key)

        # STEP 2: Configure Deepgram options for audio analysis
        self._options = PrerecordedOptions(
            model = model_name,
            smart_format = True,
        )

    def transcribe(self, audio_path: str, is_link = False) -> str:
        # Local file
        if not is_link:
            # Check file existed!
            if not os.path.exists(audio_path):
                raise Exception("File is not existed!")

            # Get buffer
            with open(audio_path, "rb") as file:
                buffer_data = file.read()

            payload: FileSource = {
                "buffer": buffer_data,
            }

            # Get response in JSON format
            response = self._client.listen.prerecorded.v("1").transcribe_file(payload, self._options)
            print(response.to_json(indent=4))
            return ""
        # Link file
        else:
            response = self._client.listen.prerecorded.v("1").transcribe_url(audio_path, self._options)
            print(response)
            return ""
