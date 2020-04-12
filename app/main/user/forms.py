# -*- coding:utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Length, DataRequired, URL
from flask_pagedown.fields import PageDownField
from flask_wtf.file import FileField, FileAllowed
from app import avatars


class EditProfileForm(FlaskForm):
    name = StringField(u'Username', validators=[DataRequired(message=u"Cannot be blank!"), Length(1, 64, message=u"Less than 64 character")])
    major = StringField(u'Major', validators=[Length(0, 128, message=u"Less than 128 characters")])
    headline = StringField(u'About Yourself', validators=[Length(0, 32, message=u"Less than 32 characters")])
    about_me = PageDownField(u"Personal Profile")
    submit = SubmitField(u"Save")


class AvatarEditForm(FlaskForm):
    avatar_url = StringField('', validators=[Length(1, 100, message=u"Length limited to 100 characters"), URL(message=u"Fill correct url")])
    submit = SubmitField(u"Save")


class AvatarUploadForm(FlaskForm):
    avatar = FileField('', validators=[FileAllowed(avatars, message=u"Only images")])
