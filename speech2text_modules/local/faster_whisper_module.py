from faster_whisper import WhisperModel
from typing import Literal,Union,Optional

class FasterWhisperModule(WhisperModel):
    def __init__(self,
                 model_size_or_path: Union[Literal["base","small","medium","large"],str] = 'base',
                 device: Literal["auto","cpu","cuda"] = "auto",
                 device_index :int = 0,
                 compute_type :Literal["int8_float32","int8","int8_float16","int8_bfloat16","int16","float16","bfloat16","float32"] = "float16",
                 cpu_threads :int = 0,
                 num_workers :int = 1,
                 download_root :Optional[str] = None
                 ):
        super().__init__(model_size_or_path = model_size_or_path,
                         device = device,
                         device_index = device_index,
                         compute_type = compute_type,
                         cpu_threads = cpu_threads,
                         num_workers = num_workers,
                         download_root = download_root
                         )
        """model_size_or_path: Size of the model to use (tiny, tiny.en, base, base.en,
                    small, small.en, medium, medium.en, large-v1, large-v2, large-v3, or large), a path to a
                    converted model directory, or a CTranslate2-converted Whisper model ID from the HF Hub.
                    When a size or a model ID is configured, the converted model is downloaded
                    from the Hugging Face Hub."""