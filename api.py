import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/app', methods=['GET'])
def home():
    return "<h1>First Python App</h1><p>First web app in python</p>"

app.run(port=5000)