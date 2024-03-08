# Base image
FROM python:3.11

# Working Dir
WORKDIR /code

# Requirements 
COPY ./requirements.txt /code/requirements.txt

# Install
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy relevant files
COPY . /code

# Run fastapi
CMD ["uvicorn", "asr_api:app", "--host", "0.0.0.0", "--port", "8001"]