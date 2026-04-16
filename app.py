from flask import Flask, jsonify, request

app = Flask(__name__)

items = []

@app.route("/")
def home():
    return "Still alive!", 200

@app.route("/health")
def health():
    return jsonify({"status": "ok"}, 200)

@app.route("/items", methods=["GET"])
def get_items():
    return jsonify(items)

@app.route("/items", methods=["POST"])
def add_items():
    data = request.json
    items.append(data)
    return jsonify(data), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)