from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class BookForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    author = StringField("Author", validators=[DataRequired()])
    genre = StringField("Genre")
    condition = SelectField("Condition", choices=[("new","New"),("used","Used")])
    description = TextAreaField("Description")
    submit = SubmitField("Add Book")