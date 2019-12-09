from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def initialize():
    return '<h1>Test</h1>'

@app.route('/test_put', methods=['PUT'])
def put_testing():
    return "this works"

@app.route('/test_get', methods=['GET'])
def get_testing():
    return "this works"

if __name__ == '__main__':
    app.run(threaded=False)
