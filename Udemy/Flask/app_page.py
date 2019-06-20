import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_word():
    return 'hello world'

if __name__ == '__main__':
    host = os.getenv('IP', 'localhost')
    port = int(os.getenv('PORT', 8000))
    app.run(host=host, port=port)