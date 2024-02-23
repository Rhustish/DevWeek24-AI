import main 
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET', 'POST'])
def my_api():
    if request.method == 'GET':
        return jsonify({"message": "Hello, World!"})
    elif request.method == 'POST':
        data = request.get_json()
        return jsonify({"received": data}), 201

if __name__ == '__main__':
    app.run(debug=True, port=4000)

