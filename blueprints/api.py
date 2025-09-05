from flask import Blueprint, jsonify, request
from utils.helpers import parse_resume, translate_content as translate_text, get_price_for_country

api_bp = Blueprint('api', __name__)

@api_bp.route('/data')
def get_data():
    data = {
        "message": "API response",
        "status": "success"
    }
    return jsonify(data)

@api_bp.route('/users')
def get_users():
    users = [
        {"id": 1, "name": "User 1"},
        {"id": 2, "name": "User 2"}
    ]
    return jsonify(users)

@api_bp.route('/portfolio', methods=['POST'])
def upload_portfolio():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
        
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
        
    if file and file.filename and (file.filename.endswith('.pdf') or file.filename.endswith('.doc') or file.filename.endswith('.docx')):
        portfolio_data = parse_resume(file)
        return jsonify(portfolio_data)
    
    return jsonify({"error": "File type not allowed"}), 400

@api_bp.route('/translate', methods=['POST'])
def translate_content():
    data = request.json
    
    if not data:
        return jsonify({"error": "No JSON content provided"}), 400
    
    target_lang = request.args.get('target_lang', 'en')
    translated_data = translate_text(data, target_lang)
    
    return jsonify(translated_data)

@api_bp.route('/pricing', methods=['GET'])
def get_pricing():
    country = request.args.get('country', 'US')
    pricing_data = get_price_for_country(country)
    
    return jsonify(pricing_data)
