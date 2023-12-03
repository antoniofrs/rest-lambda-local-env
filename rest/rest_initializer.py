import json
from flask import Flask, request
from rest.model.route import HttpMethod, Route
from rest.route_initializer import find_function, init_config


app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    catched_method = request.method,
    catched_path = f"/{path}"
    function = find_function(catched_method, catched_path)


def init_flask():
    config_port = init_config()
    app.run(host="0.0.0.0", port=config_port)



