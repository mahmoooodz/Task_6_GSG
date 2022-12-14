import json

import jinja2
from jinja2 import Environment, FileSystemLoader
import requests
from flask import Flask,render_template
app = Flask(__name__)

@app.route("/students.html")
def home():
    result = requests.get("http://staging.bldt.ca/api/method/build_it.test.get_students")
    result = json.loads(result.text)
    data = result.get('data')
    context = {}
    context['students'] = data
    return render_template("students.html", **context)


app.run(debug=True)