import os
import requests
from flask.ext.sqlalchemy import SQLAlchemy

from flask import Flask, render_template, request
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

from models import *

@app.route("/", methods=["GET", "POST"])
def index():
    errors = []
    results = {}
    if request.method == "POST":
        try:
            url = request.form['url']
            r = requests.get(url)
            print r.text
        except:
            errors.append(
                "Unable to get URL"        
            )
    print(os.environ['APP_SETTINGS'])
    return render_template('index.html', errors=errors, results=results)


if __name__ == "__main__":
    app.run()
