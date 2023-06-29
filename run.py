#!/usr/bin/python

from flask import Flask, jsonify, render_template, request, url_for


app = Flask(__name__)


@app.route('/')
def index():
    h = "Home"
    return render_template('home.html',home=h)

if __name__ == '__main__':
    #app.run()
    app.run(host='0.0.0.0', port=4999, debug=True)
