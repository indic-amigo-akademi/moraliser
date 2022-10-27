from flask import request, jsonify, current_app
from chat.api import api_bp
from chat.forms import RegisterForm
from chat.models import db, User


@api_bp.route('/login', methods=['POST'])
def user_login():
    username = request.form.get('username')
    password = request.form.get('password')
    return jsonify({"message": "Logged in successfully!", "status": "success"})


@api_bp.route('/register', methods=['POST'])
def user_register():
    try:
        form = RegisterForm()
        if form.validate_on_submit():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            phone = form.phone.data
            newUser = User(email=email,
                           username=username,
                           password=password,
                           phone=phone)
            db.session.add(newUser)
            db.session.commit()
            return jsonify({
                "message": "Registered successfully!",
                "success": True
            })
        if form.errors != {}:
            return jsonify({
                "message": "Error during registration!",
                "errors": form.errors,
                "success": False
            })

    except Exception as e:
        current_app.logger.error('>>> Error {}'.format(e))
        return jsonify({
            "message": "Error during registration!",
            "errors": str(e),
            "success": False
        })


@api_bp.route('/logout', methods=['POST'])
def user_logout():
    return jsonify({
        "message": "Logged out successfully!",
        "status": "success"
    })
