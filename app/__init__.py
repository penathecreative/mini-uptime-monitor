from flask import Flask
from app.routes import main
from app.monitor import start_monitor

def create_app():
    print("Creating Flask app...")
    app = Flask(__name__)
    app.register_blueprint(main)
    start_monitor()
    return app
