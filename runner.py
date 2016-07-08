import os
from flask import Flask, render_template
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

@app.route("/", methods=["GET", "POST"])
def index():
    print(os.environ['APP_SETTINGS'])
    return render_template('index.html')


if __name__ == "__main__":
    app.run()
