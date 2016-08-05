import os
import re
import requests
import operator
import nltk
from stop_words import stops
from flask.ext.sqlalchemy import SQLAlchemy
from collections import Counter
from bs4 import BeautifulSoup
from rq import Queue
from rq.job import Job
from worker import conn
from word_counter import *

from flask import Flask, render_template, request
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

q = Queue(connection=conn)

from models import *

@app.route("/", methods=["GET", "POST"])
def index():
    results = {}
    if request.method == "POST":
        # import pdb;pdb.set_trace()
        app.logger.error('Request body=')
        app.logger.error(str(request.json))
        # get url that the person has entered
        url = request.form['url']
        if 'http://' not in url[:7]:
            url = 'http://' + url
        job = q.enqueue_call(
            func=count_and_save, args=(url,), result_ttl=5000
        )
        print(job.get_id())

    return render_template('index.html', results=results)

@app.route("/results/<job_key>", methods=['GET'])
def get_results(job_key):

    job = Job.fetch(job_key, connection=conn)

    if job.is_finished:
        return str(job.result), 200
    else:
        return "Nay!", 202

if __name__ == "__main__":
    app.run()
