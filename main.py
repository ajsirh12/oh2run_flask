from flask import Flask
from constants.server import Server
import controller.controller_main as mc

app = Flask(__name__)

# jsonify 한글깨짐 방지
app.config['JSON_AS_ASCII'] = False
app.register_blueprint(mc.app)

if __name__ == "__main__":
    app.run(host=Server.HOST.value, port=Server.PORT.value)