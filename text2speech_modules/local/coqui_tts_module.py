import torch,os
from TTS.api import TTS
from config import transcript_params
from strenum import StrEnum
from typing import Union,Optional

class EnglishTTSModel(StrEnum):
    TACOTRON2 = "tts_models/en/ljspeech/tacotron2-DDC",
    GLOW = "tts_models/en/ljspeech/glow-tts",
    SPEEDY_SPEECH = "tts_models/en/ljspeech/speedy-speech",
    FAST_PITCH = "tts_models/en/ljspeech/fast_pitch",
    OVER_FLOW = "tts_models/en/ljspeech/overflow"

class CoquiTTSModule():
    def __init__(self,
                 model_name: Union[EnglishTTSModel,str] = EnglishTTSModel.TACOTRON2,
                 language: str = "default"):
        """Initialize gTTS Text to speech Module with specific params.
        - model_name: Specify model name, use tts --list_models for getting more information
        - speaker_wav: Optional params. Only use for multi lingual model.
        - lang: Useful when working with multilingual model. Default is default
        """

        # Initialize path
        os.makedirs(transcript_params.audio_directory, exist_ok=True)

        # Initialize client
        self.__device = "cuda" if torch.cuda.is_available() else "cpu"
        self._enable_gpu = True if self.__device == "cuda" else False
        self._client = TTS(model_name=model_name,
                           progress_bar=True,
                           gpu = self._enable_gpu).to(self.__device)
        # Define params
        self._language = language

    def generate(self,
                 transcript :str,
                 speaker_wav :Optional[str] = None,
                 file_name: str = "sample.mp3") -> None:
        # List of audio format
        audio_extensions = ["mp3","wav"]
        audio_extensions = [f".{ext}" for ext in audio_extensions]

        # Check logic
        if self._language != "default" and speaker_wav == None:
            raise Exception("Multi-lingual model must be specify speaker_wav params")

        # Validate
        assert isinstance(transcript,str), "Text must be string"
        # Check format
        extension = os.path.splitext(file_name)[-1]
        if extension not in audio_extensions:
            raise Exception("Wrong audio path. Must be end at .mp3 or .wav format!")

        # Define saved path
        saved_path = os.path.join(transcript_params.audio_directory, file_name)
        # Initialize object
        if speaker_wav == None:
            self._client.tts_to_file(text = transcript, file_path = saved_path)
        else:
            self._client.tts_to_file(text = transcript,
                                     speaker_wav = speaker_wav,
                                     language = self._language,
                                     file_path = saved_path)

