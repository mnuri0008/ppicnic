
import os
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-secret")
    app.config["MAX_USERS"] = int(os.environ.get("MAX_USERS", "50"))
    return app

app = create_app()
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="eventlet")

@app.route("/")
def index():
    return render_template("index.html", max_users=app.config["MAX_USERS"])

@socketio.on("connect")
def on_connect():
    emit("server_message", {"msg": "Connected to NURI Piknik v5 🎉"})

@socketio.on("ping_server")
def on_ping(data):
    emit("server_message", {"msg": f"PONG: {data}"}, broadcast=True)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    socketio.run(app, host="0.0.0.0", port=port)
