import math
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.get_json()
    expression = data.get("expression", "")

    try:
        # Define safe operations
        allowed_names = {
            k: v for k, v in math.__dict__.items() if not k.startswith("__")
        }
        allowed_names["abs"] = abs
        allowed_names["round"] = round

        # Evaluate safely
        result = eval(expression, {"__builtins__": {}}, allowed_names)
    except Exception:
        result = "Error"

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True, port=5001)
