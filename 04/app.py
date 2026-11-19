from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/greet', methods=['GET'])
def greet():
    name = request.args.get('name')

    if name:
        message = f"Hello, {name}!"
    else:
        message = "Hello!"

    return jsonify({"message": message})


if __name__ == '__main__':
    app.run(debug=True)
