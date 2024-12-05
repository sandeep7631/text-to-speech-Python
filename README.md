# Text-to-Speech Application

This is a Python-based Text-to-Speech (TTS) application that uses Flask for the web framework, 
gTTS for generating speech, and Pygame for playing the audio. It provides a simple interface 
for users to input text and hear the corresponding audio output.

## Features

- **Web Interface**: Input text via a web form hosted using Flask.
- **Text-to-Speech Conversion**: Converts text into audio using the Google Text-to-Speech (gTTS) library.
- **Audio Playback**: Plays the generated speech using the Pygame library.

## Project Structure

```
tts/
├── app.py           # Main Flask application
├── templates/
│   └── index.html   # HTML template for the web interface
├── tts.py           # Script for standalone TTS functionality
├── welcome.mp3      # Example audio file
```

## Requirements

- Python 3.x
- Flask
- gTTS
- Pygame

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sandeep7631/text-to-speech-Python.git
   ```
2. Navigate to the project directory:
   ```bash
   cd text-to-speech-Python
   ```
3. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Run the Flask Application
1. Start the Flask server:
   ```bash
   python app.py
   ```
2. Open your browser and navigate to `http://127.0.0.1:5000`.
3. Enter text into the input field and press "Submit" to hear the generated speech.

### Run the TTS Script
1. Execute the `tts.py` script for a standalone TTS functionality:
   ```bash
   python tts.py
   ```
2. Follow the on-screen instructions to enter text and generate speech.

## Demo

The web interface allows you to input text and listen to the corresponding audio directly in your browser.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/): A lightweight WSGI web application framework.
- [gTTS](https://gtts.readthedocs.io/): A Python library and CLI tool to interface with Google Translate's text-to-speech API.
- [Pygame](https://www.pygame.org/): A cross-platform set of Python modules designed for writing video games, but also used for multimedia applications.

## Screenshots
![image](https://github.com/user-attachments/assets/c5864b65-5ba0-4675-bdc9-0bdd4f0db29e)

![image](https://github.com/user-attachments/assets/9ab15d85-bca7-4d0e-9acb-504abb323751)

