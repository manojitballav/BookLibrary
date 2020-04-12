# -*- coding:utf-8 -*-
from app.models import Book
from flask_pagedown.fields import PageDownField
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms import ValidationError
from wtforms.validators import Length, DataRequired, Regexp


class EditBookForm(FlaskForm):
    isbn = StringField(u"ISBN",
                       validators=[DataRequired(message=u"Cannot be blank!"),
                                   Regexp('[0-9]{13,13}', message=u"ISBN must be 13 digits")])
    title = StringField(u"Title",
                        validators=[DataRequired(message=u"Cannot be blank!"), Length(1, 128, message=u"Must be of 1 to 128 characters")])
    origin_title = StringField(u"Original Name", validators=[Length(0, 128, message=u"Must be of 0 to 128 characters")])
    subtitle = StringField(u"Subtitle", validators=[Length(0, 128, message=u"Must be of 0 to 128 characters")])
    author = StringField(u"Author", validators=[Length(0, 128, message=u"Must be of 0 to 64 characters")])
    translator = StringField(u"Translator",
                             validators=[Length(0, 64, message=u"Must be of 0 to 64 characters")])
    publisher = StringField(u"Publisher", validators=[Length(0, 64, message=u"Must be of 0 to 64 characters")])
    image = StringField(u"Image Address", validators=[Length(0, 128, message=u"Must be of 0 to 128 characters")])
    pubdate = StringField(u"Date of Publishing", validators=[Length(0, 32, message=u"Must be of 0 to 32 characters")])
    tags = StringField(u"Tags", validators=[Length(0, 128, message=u"Must be of 0 to 128 characters")])
    pages = IntegerField(u"Number of Pages")
    price = StringField(u"Price", validators=[Length(0, 64, message=u"Must be of 0 to 64 characters")])
    binding = StringField(u"Binding", validators=[Length(0, 16, message=u"Must be of 0 to 16 characters")])
    numbers = IntegerField(u"Collection", validators=[DataRequired(message=u"Cannot be blank!")])
    summary = PageDownField(u"Summary")
    catalog = PageDownField(u"Directory")
    submit = SubmitField(u"Add")


class AddBookForm(EditBookForm):
    def validate_isbn(self, filed):
        if Book.query.filter_by(isbn=filed.data).count():
            raise ValidationError(u'This book already exisit')


class SearchForm(FlaskForm):
    search = StringField(validators=[DataRequired()])
    submit = SubmitField(u"Search")


