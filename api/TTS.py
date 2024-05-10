from fastapi import APIRouter, HTTPException
from functions.text_to_speech import generate_speech
from kafka.consumer import consume_messages

router = APIRouter()

# endpoint for get speech
@router.get("/text_to_speech")
async def text_to_speech():
    try:
        text = consume_messages()
        speech = generate_speech(text)

        return {
            "text": text,
            "audio_base64" : speech
        }
    
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))