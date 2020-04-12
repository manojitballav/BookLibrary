# -*- coding:utf-8 -*-
from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import Length, DataRequired


class CommentForm(FlaskForm):
    comment = TextAreaField(u"Your Book Review",
                            validators=[DataRequired(message=u"Cannot be empty"), Length(1, 1024, message=u"Limited to 1024 characters")])
    submit = SubmitField(u"Submit")