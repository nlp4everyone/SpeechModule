from speech2text_modules.intergrations import GroqTranscriptModule
import time

transcript_module = GroqTranscriptModule()
begin = time.time()
transcript_module.transcribe(audio_path = "Actor_01/03-01-01-01-01-01-01.wav")
end = time.time() - begin
print(end)