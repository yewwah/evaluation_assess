import pandas as pd
from transformers import pipeline
import torch
from tqdm import tqdm
import librosa

# Progress report 
tqdm.pandas()
 
 # load model and processor

# Pipeline initialization
# Chunking to reduce memory usage and stride length to provide more context. Reference : https://huggingface.co/blog/asr-chunking
pipe = pipeline("automatic-speech-recognition", model="facebook/wav2vec2-large-960h",  chunk_length_s = 10, stride_length_s=(4,2))

# Transcribing based on zip files
def transcribe(fname : str) -> str:
    print('cv-valid-dev/' + fname)
    # Loading the audio
    audio, _ = librosa.load('cv-valid-dev/' + fname, sr = 16000)
    # returning the result 
    return pipe(audio)['text']
    

df = pd.read_csv('cv-valid-dev.csv')
df['generated_text'] = df['filename'].progress_apply(transcribe)
df.to_csv('cv-valid-dev.csv', index=False)

