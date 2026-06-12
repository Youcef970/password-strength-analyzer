from flask import Flask, render_template, request, jsonify
from analyzer import analyze_password
from generator import generate_strong_password

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    password = data.get('password', '')
    result = analyze_password(password)
    return jsonify(result)

@app.route('/generate', methods=['GET'])
def generate():
    password = generate_strong_password(18)
    return jsonify({'password': password})

if __name__ == '__main__':
    app.run(debug=True)