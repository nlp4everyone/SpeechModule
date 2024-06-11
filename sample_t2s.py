from text2speech_modules.intergrations import CartesiaT2SModule
# from text2speech_modules.local import CoquiTTSModule
transcript = "Hello, what can i help you?"

# Define Service Speech to Text intergration module
module = CartesiaT2SModule()
# Generate text
module.generate(transcript = transcript)

# Define Service Speech to Text intergration module
# module = CoquiTTSModule()
# # Generate text
# module.generate(transcript = transcript)