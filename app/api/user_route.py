from flask import request, jsonify
from . import api_bp


@api_bp.route('/login', methods=['POST'])
def user_login():
    username = request.form.get('username')
    password = request.form.get('password')
    return jsonify({"msg": "Logged in successfully!", "status": "success"})


@api_bp.route('/register', methods=['POST'])
def user_register():
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')
    return jsonify({"msg": "Registered successfully!", "status": "success"})

@api_bp.route('/logout', methods=['POST'])
def user_logout():
    return jsonify({"msg": "Logged out successfully!", "status": "success"})
