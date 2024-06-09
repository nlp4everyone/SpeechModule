from speech2text_modules.intergrations import GroqTranscriptModule

path = "audio_samples/sample_1.wav"

# Define Speech to Text module
groq_module = GroqTranscriptModule()
text = groq_module.transcribe(audio_path = path)
print(text)
