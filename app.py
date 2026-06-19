import os
from flask import Flask, jsonify

app = Flask(__name__)
VERSION = "v2"

@app.route("/")
def index():
    return f"Gritiva E2E test app — {VERSION}\n"

@app.route("/health")
def health():
    return jsonify(status="ok", version=VERSION)

@app.route("/info")
def info():
    return jsonify(app="gritiva-e2e", version=VERSION, endpoints=["/", "/health", "/info"])
