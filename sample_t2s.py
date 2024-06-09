from text2speech_modules.intergrations import CartesiaTranscriptModule

transcript = "Hello, what can i help you?"

# Define Service Speech to Text module
cartesia_module = CartesiaTranscriptModule()
# Generate text
cartesia_module.generate(transcript = transcript)
