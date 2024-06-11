from text2speech_modules.intergrations import CartesiaT2SModule
import time
transcript = "Hello, what can i help you?"

# Define Service Speech to Text module
t2s = CartesiaT2SModule()
# Generate text
beginTime = time.time()
t2s.generate(transcript = transcript)
endTime = time.time() - beginTime