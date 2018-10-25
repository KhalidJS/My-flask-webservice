from flask import Flask, jsonify, render_template, request, url_for
#from RandomStuff import LED_Blink


app = Flask(__name__)
app.config.from_object('config')


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
            return "Blinking!"
    return render_template("blink.html")


if __name__ == '__main__':
    app.run()
    app.add_url_rule('/favicon.ico', redirect_to=url_for('static', filename='favicon.ico'))