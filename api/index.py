from flask import Flask, request, jsonify
from flask_cors import CORS
from deep_translator import GoogleTranslator

app = Flask(__name__)
CORS(app)  # Enable CORS for all origins

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


if __name__ == '__main__':
    app.run(debug=True)
