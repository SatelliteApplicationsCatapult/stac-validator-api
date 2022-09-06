from validate import StacValidate
from flask import Flask, request, jsonify
import json

app = Flask(__name__)


@app.route("/", methods=["POST"])
def validate():
    data = request.get_json()
    json_data = json.loads(data)
    stac = StacValidate(
        json_input=json_data,
    )
    stac.run()
    message = stac.message
    return jsonify(message)


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=6789)
