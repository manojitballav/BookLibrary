# -*- coding:utf-8 -*-
from app import db
from app.models import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms import ValidationError
from wtforms.validators import Email, Length, DataRequired, EqualTo


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(message=u"Cannot be blank!"), Length(1, 64), Email(message=u"Correct Email ?")])
    password = PasswordField(u'password', validators=[DataRequired(message=u"Cannot be blank!"), Length(6, 32)])
    remember_me = BooleanField(u"Keep logged in", default=True)
    submit = SubmitField(u'Log In')


class RegistrationForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(message=u"Cannot be blank!"), Length(1, 64), Email(message=u"Correct Email ?")])
    name = StringField(u'username', validators=[DataRequired(message=u"Cannot be blank!"), Length(1, 64)])
    password = PasswordField(u'password',
                             validators=[DataRequired(message=u"Cannot be blank!"), EqualTo('password2', message=u'Passwords must match'),
                                         Length(6, 32)])
    password2 = PasswordField(u'Confirm password again', validators=[DataRequired(message=u"Cannot be blank!")])
    submit = SubmitField(u'Register')

    def validate_email(self, filed):
        if User.query.filter(db.func.lower(User.email) == db.func.lower(filed.data)).first():
            raise ValidationError(u'Email has been registered')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField(u'Current password', validators=[DataRequired(message=u"Cannot be blank!")])
    new_password = PasswordField(u'New password', validators=[DataRequired(message=u"Cannot be blank!"),
                                                     EqualTo('confirm_password', message=u'Passwords must match'),
                                                     Length(6, 32)])
    confirm_password = PasswordField(u'Confirm New Password', validators=[DataRequired(message=u"Cannot be blank!")])
    submit = SubmitField(u"Saved")

    def validate_old_password(self, filed):
        from flask_login import current_user
        if not current_user.verify_password(filed.data):
            raise ValidationError(u'Wrong Password')
