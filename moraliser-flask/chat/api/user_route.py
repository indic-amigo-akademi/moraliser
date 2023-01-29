from flask import request, jsonify, current_app
from chat.api import api_bp
from chat.forms import LoginForm, RegisterForm
from chat.models import db, User
from flask_login import login_user, logout_user, current_user
from flask_wtf.csrf import generate_csrf, validate_csrf


@api_bp.route("/current", methods=["GET"])
def get_current_user():
    user = None
    message = "No current user found!"
    success = True
    if current_user.is_active:
        user = current_user.serialize
        message = "Current user found!"

    return jsonify(
        {
            "success": success,
            "message": message,
            "data": {"user": user, "csrf_token": generate_csrf()},
        }
    )


@api_bp.route("/my-csrf", methods=["GET"])
def get_csrf_token():
    return jsonify(
        {
            "success": True,
            "message": "CSRF Token is here!",
            "data": {"csrf_token": generate_csrf()},
        }
    )


@api_bp.route("/validate-csrf", methods=["GET"])
def validate_csrf_token():
    csrf_token = request.args.get("csrf_token")
    try:
        validate_csrf(csrf_token)
        return jsonify(
            {"success": True, "message": "CSRF Token is valid", "data": None}
        )
    except Exception as e:
        return jsonify({"success": False, "message": str(e), "data": None})


@api_bp.route("/login", methods=["POST"])
def user_login():
    try:
        form = LoginForm()

        if form.validate_on_submit():
            attempted_user = User.query.filter_by(username=form.username.data).first()

            if attempted_user and attempted_user.check_password(
                attempted_password=form.password.data
            ):
                login_user(attempted_user)

                return jsonify(
                    {
                        "success": True,
                        "message": "Logged in successfully!",
                        "data": None,
                    }
                )
            else:
                return jsonify(
                    {
                        "success": False,
                        "message": "Error during logging!",
                        "data": {
                            "errors": {
                                "all": [
                                    "Username and password are not match! Please try again."
                                ]
                            }
                        },
                    }
                )
        if form.errors != {}:
            return jsonify(
                {
                    "success": False,
                    "message": "Error during logging!",
                    "data": {
                        "errors": form.errors,
                    },
                }
            )

    except Exception as e:
        current_app.logger.error(">>> Error {}".format(e))
        return jsonify(
            {
                "success": False,
                "message": "Error during logging!",
                "data": {"errors": {"all": [str(e)]}},
            }
        )


@api_bp.route("/register", methods=["POST"])
def user_register():
    try:
        form = RegisterForm()

        if form.validate_on_submit():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            phone = form.phone.data
            newUser = User(
                email=email, username=username, password=password, phone=phone
            )
            db.session.add(newUser)
            db.session.commit()
            login_user(newUser)
            return jsonify(
                {"success": True, "message": "Registered successfully!", "data": None}
            )

        if form.errors != {}:
            return jsonify(
                {
                    "success": False,
                    "message": "Error during registration!",
                    "data": {
                        "errors": form.errors,
                    },
                }
            )

    except Exception as e:
        current_app.logger.error(">>> Error {}".format(e))
        return jsonify(
            {
                "success": False,
                "message": "Error during registration!",
                "data": {"errors": {"all": [str(e)]}},
            }
        )


@api_bp.route("/logout", methods=["POST"])
def user_logout():
    logout_user()
    return jsonify(
        {"success": True, "message": "Logged out successfully!", "data": None}
    )
