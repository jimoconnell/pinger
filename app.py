from flask import Flask, jsonify, render_template
from flask_cors import CORS
import subprocess
import re

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ping/<host>')
def ping(host):
    try:
        output = subprocess.check_output(f"ping -c 1 {host}", stderr=subprocess.STDOUT, shell=True, text=True)
        time = float(re.search("time=([\d.]+)", output).group(1))
        return jsonify({'success': True, 'time': time})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

