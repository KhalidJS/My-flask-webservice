#!/usr/bin/python

from flask import Flask, jsonify, render_template, request, url_for
from RandomStuff import Traffic_Light


app = Flask(__name__)


@app.route('/')
def index():
    return "Hello There!"


@app.route('/<name>')
def get_name(name):
    return 'Hello {}!'.format(name)


@app.route('/data', methods=['GET'])
def names():
    if request.method == 'GET':
        data = {"Names": ["Anna", "Joanna", "Thomas", "CK", "John", "Mick"]}
        return jsonify(data)
    return


@app.route('/blink', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        if request.form.get('Blinky') == 'blink':
            print("blinking!!")
            x = Traffic_Light.TrafficLight(2, 4, 21)
            x.start_traffic_light(True)
    return render_template("blink.html")


if __name__ == '__main__':
    #app.run()
    app.run(host='0.0.0.0', port=4999, debug=True)
