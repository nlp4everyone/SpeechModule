from dotenv import load_dotenv
import os
load_dotenv()
audio_directory = "SavedAudio"

# Define params
ASSEMBLYAI_KEY = os.getenv("ASSEMBLYAI_KEY")
DEEPGRAM_KEY = os.getenv("DEEPGRAM_KEY")
GROQ_KEY = os.getenv("GROQ_KEY")
CARTERSIA_KEY = os.getenv("CARTERSIA_KEY")
