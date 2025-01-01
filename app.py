from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hey, Python-flask app is successfully deployed on docker container'

@app.route('/health')
def health():
    return 'Server is up and running'
