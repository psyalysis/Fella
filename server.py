from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on("gyro_data")
def handle_gyro_data(data):
    """Receives gyroscope data from phone and sends it to all connected clients."""
    socketio.emit("update_display", data)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
