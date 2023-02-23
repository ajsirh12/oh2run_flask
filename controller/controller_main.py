from flask import Blueprint, jsonify
import json
from utils.core import Logger

app = Blueprint('main', __name__)
logger = Logger.get_log()

@app.route('/', methods=['GET'])
def home():
    logger.info("hello world")
    return "Hello wolrd()!"