from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, URLField, SubmitField
from wtforms.validators import DataRequired, Optional, URL

class BookForm(FlaskForm):
    title = StringField("Название", validators=[DataRequired()])
    author = StringField("Автор", validators=[DataRequired()])
    genre = StringField("Жанр", validators=[Optional()])
    condition = SelectField("Состояние", choices=[("new", "Новая"), ("used", "Б/у")])
    description = TextAreaField("Описание", validators=[Optional()])
    link = URLField("Ссылка на онлайн-версию", validators=[Optional(), URL(message="Неверный формат URL")])  # ← новое поле
    submit = SubmitField("Добавить книгу")