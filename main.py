from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return "Hello world!"

if __name__ == "__main__":
    app.run(host='localhost', port='3100')