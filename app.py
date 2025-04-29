from flask import Flask
from flask_cors import CORS
from routes.generate import generate_bp
from routes.upload import upload_bp
import os

app = Flask(__name__)

# Configure CORS to allow requests from Vercel with specific methods
allowed_origins = os.getenv('ALLOWED_ORIGINS', '*')
CORS(
    app,
    origins=allowed_origins.split(','),
    methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],  # Explicitly allow methods
    allow_headers=['Content-Type', 'Authorization']      # Allow common headers
)

app.register_blueprint(generate_bp, url_prefix="/api")
app.register_blueprint(upload_bp, url_prefix="/api")