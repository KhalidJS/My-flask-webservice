from flask import Flask, jsonify, render_template, request, url_for
import socket
from gpiozero import LED


app = Flask(__name__)
hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)
print(IP)


@app.route('/')
def index():
    return "Hello There!"


@app.route('/<name>')
def get_name(name):
    return 'Hello {}!'.format(name)


@app.route('/data', methods=['GET'])
def names():
    if request.method == 'GET':
        data = {"Names": ["Anna", "Joanna", "Thomas", "CK", "John"]}
        return jsonify(data)
    return


@app.route('/blink', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        if request.form.get('Blinky') == 'blink':
            print("blinking!!")
            led = LED(2)
            led.blink(2, 1)
    return render_template("blink.html")


if __name__ == '__main__':
    #app.run()
    app.run(host='0.0.0.0', port=80, debug=True)