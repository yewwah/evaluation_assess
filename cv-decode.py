import pandas as pd
from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC, pipeline
import torch
from tqdm import tqdm
import librosa
# from tqdm.auto import tqdm  # for notebooks

# Create new `pandas` methods which use `tqdm` progress
# (can use tqdm_gui, optional kwargs, etc.)
tqdm.pandas()
 
 # load model and processor

pipe = pipeline("automatic-speech-recognition", model="facebook/wav2vec2-large-960h",  chunk_length_s = 10, stride_length_s=(4,2))
# load dummy dataset and read soundfiles
def transcribe(fname : str) -> str:
    print('cv-valid-dev/' + fname)
    audio, _ = librosa.load('cv-valid-dev/' + fname, sr = 16000)
    # tokenize
    return pipe(audio)['text']
    

df = pd.read_csv('cv-valid-dev.csv')
df['generated_text'] = df['filename'].progress_apply(transcribe)
df.to_csv('cv-valid-dev-generated.csv', index=False)

