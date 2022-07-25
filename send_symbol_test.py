from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("send_symbol.html")

@app.route("/symbol", methods=["POST"])
def receive_data():
    global SYMBOLS
    print("receive_data()")
    SYMBOLS = request.form["symbols"]

    return f"<h1>SYMBOLS: {SYMBOLS}</h1>"


"""
NOTE: The action attribute of the form can be set to "/login" e.g.
<form action="/login" method="post">
or it can be dynamically generated with url_for e.g.
<form action="{{ url_for('receive_data') }}" method="post">
Depending on where your server is hosted, the "/login" path may change. 
So it's usually a better idea to use url_for to dynamically generate the url for a particular function in your Flask server.
"""

if __name__ == "__main__":
    app.run(debug=True)
