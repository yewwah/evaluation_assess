from flask import Flask, request
from typing import Dict, List

import json
app = Flask(__name__)

@app.route('/', methods=['GET'])
def ping() -> str:
    return 'pong'

@app.route('/asr', methods=['POST'])
def asr() -> Dict[str, str]: 
    fname = request.form['file']
    return {
        "transcription": "BEFORE HE HAD TIME TO ANSWER A MUCH ENCUMBERED VERA BURST INTO THE ROOM",
        "duration" : "20.7"
    }


if __name__ == '__main__':
   app.run(port=8001)