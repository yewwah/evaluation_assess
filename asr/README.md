# Task 2

This README documents the steps to run task 2. This folder uses FastAPI framework as well as librosa libraries to load the audio files

## Assumptions
1. User has `docker` rights

## Steps to run the folder

1. Run the command `docker build -t asr .`
2. Run the command `docker run -p 8001:8001 --name asr-api -d`

### Testing (Ping)

The shell command is 

`curl http://<YOUR PUBLIC IP>:8001/`

### Testing (ASR)
The shell command is 

`curl -F "file=@/path/to/file" http://<YOUR PUBLIC IP>:8001/asr`


