from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError, Regexp
from chat.models import User


class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError(
                'Username already exists! Please try a different username')

    def validate_email(self, email_to_check):
        email = User.query.filter_by(email=email_to_check.data).first()
        if email:
            raise ValidationError(
                'Email Address already exists! Please try a different email address'
            )

    username = StringField(label='User Name:',
                           validators=[Length(min=5, max=64),
                                       DataRequired()])
    email = StringField(label='Email Address:',
                        validators=[Email(), DataRequired()])
    password = PasswordField(
        label='Password:',
        validators=[
            Regexp(
                "^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$",
                message=
                "Password must contain minimum eight characters, at least one letter and one number"
            ),
            DataRequired()
        ])
    phone = StringField(label="Phone Number",
                        validators=[Length(min=10, max=15),
                                    DataRequired()])
