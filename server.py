from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

messages = []

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/send', methods=['POST'])
def send():
    data = request.get_json()
    message = data.get("message")
    if message:
        timestamp = datetime.now().strftime("%H:%M")
        messages.append(f"You [{timestamp}]: {message}")
    return '', 204

@app.route('/messages')
def get_messages():
    return jsonify(messages)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
