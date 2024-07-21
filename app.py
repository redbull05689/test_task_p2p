from flask import Flask,jsonify,request
from prometheus_client import Counter, generate_latest, start_http_server, Summary

app = Flask(__name__)

@app.route('/status', methods=['GET'])
def status():
    return jsonify({
        'status': 'OK',
        'message': 'Server is running',
        'code': 200
    }), 200

@app.route('/')
def home():
    return 'Hello, this is the home page!'

if __name__ == '__main__':
    start_http_server(8000)
    app.run(host='0.0.0.0', port=9000)
