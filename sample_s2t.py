from speech2text_modules.intergrations import GroqS2TModule

path = "audio_samples/sample_1.wav"

# Define Speech to Text module
s2t = GroqS2TModule()
text = s2t.transcribe(audio_path = path)
print(text)
