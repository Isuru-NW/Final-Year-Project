from http import client
from flask import Flask, request, jsonify
import model as m
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/prediction', methods=['POST'])
def predicting_price():
    req_json = request.json
    deaths = req_json['deaths']
    timestamp = req_json['timestamp']
    return m.predict(deaths, timestamp)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")cd client