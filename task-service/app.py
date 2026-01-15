from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify(status="Task Service OK")

@app.route("/tasks")
def tasks():
    return jsonify(["Learn Docker", "Learn CI/CD"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
