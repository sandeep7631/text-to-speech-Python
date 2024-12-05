from flask import Flask, render_template, request, jsonify
from gtts import gTTS
import pygame
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_audio', methods=['POST'])
def generate_audio():
    data = request.get_json()
    text = data.get('text', '')
    if not text:
        return jsonify({"error": "No text provided"}), 400
    
    try:
        # Generate audio file
        myobj = gTTS(text=text, lang='en', slow=False)
        audio_path = "welcome.mp3"
        myobj.save(audio_path)

        # Play the audio
        pygame.mixer.init()
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play()

        return jsonify({"message": "Audio generated and played!"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
