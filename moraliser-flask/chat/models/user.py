from chat.models import db, login_manager, bcrypt
from flask_login import UserMixin
from sqlalchemy.orm import validates


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(length=64), unique=True, nullable=False)
    email = db.Column(db.String(length=64), unique=True, nullable=False)
    password_hash = db.Column(db.String(length=64), nullable=False)
    phone = db.Column(db.String(length=15), unique=True, nullable=False)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_txt_password):
        self.password_hash = bcrypt.generate_password_hash(
            plain_txt_password).decode('utf-8')

    def check_password(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash,
                                          attempted_password)

    @property
    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "phone": self.phone
        }
