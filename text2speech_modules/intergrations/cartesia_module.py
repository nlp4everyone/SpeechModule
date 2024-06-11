import sounddevice as sd
import time
from config import transcript_params
from cartesia.tts import CartesiaTTS
from typing import Literal

class CartesiaT2SModule():
    def __init__(self,
                 api_key :str = transcript_params.CARTERSIA_KEY,
                 output_format :Literal["fp32","pcm","fp32_16000","fp32_22050","fp32_44100","pcm_16000","pcm_22050"] = "fp32",
                 voice :str = "Barbershop Man"):
        """Initialize Cartesia Text to speech Module with specific params. For more detailed, visit: https://play.cartesia.ai/"""

        assert api_key is not None
        self.__gen_cfg = dict(model_id="upbeat-moon", data_rtype='array', output_format=output_format)

        # Define client
        self._client = CartesiaTTS(api_key=api_key)
        # Get available voices
        voices = self._client.get_voices()

        # Exception
        if voice not in voices.keys():
            raise Exception("Voice not supported!")

        # Get voice id
        voice_id = voices[voice]["id"]
        # Get voice embedding
        self.__voice = self._client.get_voice_embedding(voice_id=voice_id)

    def generate(self, transcript :str):
        # generate audio
        output = self._client.generate(transcript=transcript, voice=self.__voice, stream=False, **self.__gen_cfg)

        # play audio
        buffer = output["audio"]
        rate = output["sampling_rate"]
        sd.play(buffer, rate, blocking=True)

