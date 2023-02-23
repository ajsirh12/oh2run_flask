from flask import Blueprint, jsonify
import json

app = Blueprint('main', __name__)

@app.route('/', methods=['GET'])
def home():
    return "Hello wolrd()!"