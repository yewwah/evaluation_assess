from typing import Dict
from fastapi import FastAPI, File, UploadFile, Form
import librosa
import io
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
    audio_data, _ = librosa.load(file.file, sr=16000)
    return pipe(audio_data)['text']

