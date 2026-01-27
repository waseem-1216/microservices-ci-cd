from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify(status="User Service OK")

@app.route("/users")
def users():
    return jsonify(["Alice", "Bob", "Charlie"])
@app.route("/")
def root():
    return "User Service is running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
