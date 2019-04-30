from flask import Blueprint, jsonify, request
from project import db

content_api = Blueprint('content', __name__)

@content_api.route('/api/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong'
    })
