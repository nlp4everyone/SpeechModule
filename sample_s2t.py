from speech2text_modules.intergrations import GroqS2TModule,DeepGramS2TModule
# from speech2text_modules.local import FasterWhisperS2TModule

path = "audio_samples/sample_1.wav"
# Define Speech to Text intergration module
module = DeepGramS2TModule()
text = module.transcribe(audio_path = path)
print(text)

# Define Speech to Text intergration module
# module = FasterWhisperS2TModule()
# segments, info = module.transcribe(audio = path)
#
# for segment in segments:
#     print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))