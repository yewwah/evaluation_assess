from typing import Dict
from fastapi import FastAPI, File, UploadFile, Form
import librosa
from transformers import pipeline

app = FastAPI()
pipe = pipeline("automatic-speech-recognition", model="facebook/wav2vec2-large-960h",  chunk_length_s = 10, stride_length_s=(4,2))

@app.get('/')
def ping() -> str:
    return 'pong'

@app.post("/asr")
def upload_file(file: UploadFile = File(...)):
    """
    Endpoint to upload a file via form data.
    """
    audio, _ = librosa.load(file)
    return pipe(audio)['text']

@app.post('/asr123')
def create_item(file: str = Form(...)):
    print(file)
    return {
        "transcription": "BEFORE HE HAD TIME TO ANSWER A MUCH ENCUMBERED VERA BURST INTO THE ROOM",
        "duration" : "20.7"
    }
