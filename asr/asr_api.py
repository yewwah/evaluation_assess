from typing import Dict
from fastapi import FastAPI, Form

app = FastAPI()

@app.get('/')
def ping() -> str:
    return 'pong'

@app.post('/asr')
async def create_item(file: str = Form(...)):
    print(file)
    return {
        "transcription": "BEFORE HE HAD TIME TO ANSWER A MUCH ENCUMBERED VERA BURST INTO THE ROOM",
        "duration" : "20.7"
    }
