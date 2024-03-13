import librosa
from typing import Dict
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from transformers import pipeline

# Initalizing the FastAPI 
app = FastAPI()

# Intializing the transformer pipeline
pipe = pipeline("automatic-speech-recognition", model="facebook/wav2vec2-large-960h",  chunk_length_s = 10, stride_length_s=(4,2))

@app.get('/')
def ping() -> str:
    return 'pong'

@app.post("/asr")
def upload_file(file: UploadFile = File(...), sr : int = 16000) -> Dict[str, str]:
    """
    Endpoint to upload an audio file via form data and return the transcribed text
    """
    # Loading the audio file via librosa
    audio_data, _ = librosa.load(file.file, sr=sr)
    # Getting duration
    duration = librosa.get_duration(y=audio_data, sr=sr)
    # Getting transcribed text
    transcribed = pipe(audio_data)['text']

    # Returning a JSON response
    return JSONResponse(content={"transcription": transcribed, "duration": duration})
    

