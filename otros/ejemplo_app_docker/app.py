from flask import Flask, request, abort, make_response, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def hola():
    return "Hola"


@app.route("/ping")
def ping():
    return "pong"


@app.route("/texto/<text>")
def devolver_texto(text):

    if "pass" in request.args:
        param_pass = int(request.args["pass"])

        if param_pass == 1:
            return text.lower().replace("password", "****")

    return text.lower()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
