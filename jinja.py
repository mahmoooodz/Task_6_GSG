import json

import jinja2
from jinja2 import Environment, FileSystemLoader
import requests
from flask import Flask,render_template
app = Flask(__name__)

@app.route("/template.html")
def home():
    result = requests.get("http://staging.bldt.ca/api/method/build_it.user_api.home.get_home")

    result = json.loads(result.text)
    data = result.get('data')
    print(data)
    main_categories = data.get('main_categories')
    featured_items = data.get('featured_items')
    print(main_categories)
    context = {}
    context['main_categories'] = main_categories
    context['featured_items'] = featured_items
    context ['data'] = "Jinja and Flask"
    product_1 = {
        "product_name" : "Pizza",
        "product_price" : 10,
        "product_qty" : 30
    }
    product_2 = {
        "product_name": "Coffee",
        "product_price": 30,
        "product_qty": 50
    }
    context['products'] = [product_1,product_2]
    return render_template("template.html", **context)

if __name__ == "__main__":
    app.run(debug=True)