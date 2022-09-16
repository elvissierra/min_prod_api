from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/custom", methods=["POST"])
def custom():
    payload = request.get_json()

    if payload.get("say_ayo") is True:
        output = jsonify({"message": "Ayo"})
    else:
        output = jsonify({"message": "..."})

    return output


if __name__ == "__main__":
    app.run
