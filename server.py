#!flask/bin/python
from app import app, socketio

if __name__ == "__main__":
    app.debug = True
    app.run()
    socketio.run(app)

