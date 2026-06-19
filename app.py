import os
from flask import Flask, jsonify

app = Flask(__name__)
VERSION = "v1"

@app.route("/")
def index():
    return f"Gritiva E2E test app — {VERSION}\n"

@app.route("/health")
def health():
    return jsonify(status="ok", version=VERSION)
