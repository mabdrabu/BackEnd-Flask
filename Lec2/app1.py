from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def say_hello():
    x = 'Hello world'
    return jsonify(x)

@app.route('/hello', methods=['POST'])
def post_hello():
    x = 'Hello world'
    return jsonify(x)

@app.route('/hello', methods=['PUT'])
def put_hello():
    x = 'Hello world'
    return jsonify(x)
    
@app.route('/hello', methods=['DELETE'])
def delete_hello():
    x = 'Hello world'
    return jsonify(x)





if __name__ == '__main__':
    app.run(debug=True)