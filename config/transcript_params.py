from dotenv import load_dotenv
import os,json
load_dotenv()

# Define params
ASSEMBLYAI_KEY = os.getenv("ASSEMBLYAI_KEY")
DEEPGRAM_KEY = os.getenv("DEEPGRAM_KEY")
GROQ_KEY = os.getenv("GROQ_KEY")
