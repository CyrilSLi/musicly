from flask import Flask, request, jsonify, send_file

app = Flask(__name__)
messages = []

@app.route("/send", methods=["POST"])
def send_message():
    global messages
    messages.append(request.json["notes"])
    return ""

@app.route("/messages", methods=["GET"])
def get_messages():
    return jsonify({"messages": messages})

@app.route("/")
def index():
    return send_file("index.html")

@app.route("/clear", methods=["POST"])
def clear_messages():
    global messages
    messages = []
    return ""