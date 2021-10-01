from flask import Flask, request
from flask import Flask, render_template
import os
import sys 
import time




app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/log")
def get_client:



if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080)