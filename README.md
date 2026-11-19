# 100knock
# 課題42


# pyのコード
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

# コマンド例と結果

curl http://127.0.0.1:5000/api/greet
{
  "message": "Hello!"
}
\
(base) yukisekiya@yukinoMacBook-Air 100knock % curl "http://127.0.0.1:5000/api/greet?name=Ushiama"
\
{
  "message": "Hello, Ushiama!"
}
