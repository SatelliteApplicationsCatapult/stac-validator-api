import json
from turtle import rt

from flask import Flask, request
import pystac

app = Flask(__name__)


@app.route("/", methods=["POST"])
def validate():
    data = request.get_json()
    # json_data = json.loads(data)
    try:
        pystac.validation.validate_dict(data)
        rtn = {
            "message": "Valid STAC",
        }
        return rtn, 200
    except Exception as e:
        rtn = {
            "message": str(e),
            "error_type": str(type(e))
        }
        return rtn, 200


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=7000)
