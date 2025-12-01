# app/app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Ogunrinu ECS Container"

if __name__ == "__main__":
    # Listen on 0.0.0.0 so Docker/ECS can reach it
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
