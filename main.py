from fastapi import FastAPI
from api.TTS import router

app = FastAPI()

app.include_router(router)