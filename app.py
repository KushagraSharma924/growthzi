from flask import Flask
from flask_cors import CORS
from blueprints.main import main_bp
from blueprints.api import api_bp
import os

def create_app():
    app = Flask(__name__, static_folder='static')
    CORS(app)
    
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp, url_prefix='/api')
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=8080, debug=True)
