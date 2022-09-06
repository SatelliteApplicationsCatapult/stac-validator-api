import json
import sys
import click
import ast

from validate import StacValidate
import requests

# flask server
from flask import Flask, request, jsonify

app = Flask(__name__)


def print_update_message(version):
    click.secho()
    if version != "1.0.0":
        click.secho(
            f"Please upgrade from version {version} to version 1.0.0!", fg="red"
        )
    else:
        click.secho("Thanks for using STAC version 1.0.0!", fg="green")
    click.secho()



@app.route('/', methods=['POST'])
def validate():
    data = request.get_json()
    json_data = json.loads(data)
    
    stac = StacValidate(
        json_input=json_data,
    )
    stac.run()
    message = stac.message
    print('Message: ', message)
    return jsonify(message)


if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=6789)