from flask import Flask, request, jsonify
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.get_json()

    if not data or 'text' not in data:
        return jsonify({'error': 'Missing text in request'}), 400

    original_text = data['text']

    try:
        # Translate the text from English to Arabic using GoogleTranslator
        translated_text = GoogleTranslator(source='en', target='ar').translate(original_text)
        return jsonify({'translated_text': translated_text})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Required for Vercel to detect the Flask app
handler = app
