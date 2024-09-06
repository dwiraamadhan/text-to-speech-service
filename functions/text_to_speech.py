from openai import OpenAI
import os, base64
from dotenv import load_dotenv


load_dotenv()

def generate_speech(text):
    client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

    speech_file_path = os.getenv("SPEECH_FILE_PATH")
    with client.audio.speech.with_streaming_response.create(
        model =  os.getenv("TEXT_TO_SPEECH_MODEL"),
        voice = os.getenv("SPEAKER_VOICE"),
        input = text
    ) as response:
        response.stream_to_file(speech_file_path)
    
    with open(speech_file_path, "rb") as audio_file:
        audio_bytes = audio_file.read()

    audio_base64 = base64.b64encode(audio_bytes).decode("utf-8")
    print(audio_base64)
    return audio_base64

# text_to_speech("BNI Direct is a service bank account for corporation that provide by BNI Bank")
