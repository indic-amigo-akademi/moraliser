from flask import request, jsonify, current_app
from chat.api import api_bp
from chat.forms import LoginForm, RegisterForm
from chat.models import db, User
from flask_login import login_user, logout_user, current_user


@api_bp.route('/current', methods=['POST'])
def get_current_user():
    user = None
    if current_user.is_active:
        user = current_user.serialize
    return jsonify({"user": user, "success": True})


@api_bp.route('/login', methods=['POST'])
def user_login():
    try:
        form = LoginForm()

        if form.validate_on_submit():
            attempted_user = User.query.filter_by(
                username=form.username.data).first()

            if attempted_user and attempted_user.check_password(
                    attempted_password=form.password.data):
                login_user(attempted_user)

                return jsonify({
                    "message": "Logged in successfully!",
                    "success": True
                })
            else:
                return jsonify({
                    "message": "Error during logging!",
                    "errors": {
                        "all": [
                            "Username and password are not match! Please try again."
                        ]
                    },
                    "success": False
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
            "message": "Error during logging!",
            "errors": {
                "all": [str(e)]
            },
            "success": False
        })


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
            login_user(newUser)
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
            "errors": {
                "all": [str(e)]
            },
            "success": False
        })


@api_bp.route('/logout', methods=['POST'])
def user_logout():
    logout_user()
    return jsonify({"message": "Logged out successfully!", "success": True})
