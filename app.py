from cProfile import run
from distutils.log import debug
from flask import Flask, request, jsonify, render_template
import pickle

#creating flask app
app = Flask(__name__)

#creating routes
@app.route('/')
def home():
    # return "Hello World"
    return render_template("index.html")


#main
if __name__ == "__main__":
    app.run(debug=True)