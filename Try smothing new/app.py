from flask import Flask, render_template, jsonify
import secrets
import string

app = Flask(__name__)

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_password/<int:length>')
def generate_password(length):
    password = generate_random_password(length)
    return jsonify({'password': password})

if __name__ == '__main__':
    app.run(debug=True)
