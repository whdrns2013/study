from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/say-hello', methods=['POST'])
def say_hello():
    data = request.json
    name = data.get('name', 'Guest')
    return jsonify({"message": f"Hello, {name}!"})

def run_rest_server():
    print("REST server started on port 5000.")
    app.run(port=5000)

if __name__ == '__main__':
    run_rest_server()