from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, URLField, SubmitField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Optional, URL

class BookForm(FlaskForm):
    title = StringField(
        "Название",
        validators=[DataRequired(message="Укажите название книги")]
    )
    author = StringField(
        "Автор",
        validators=[DataRequired(message="Укажите автора")]
    )
    genre = StringField("Жанр", validators=[Optional()])
    condition = SelectField(
        "Состояние",
        choices=[("new", "Новая"), ("used", "Б/у")]
    )
    description = TextAreaField("Описание", validators=[Optional()])
    link = URLField(
        "Ссылка на онлайн-версию",
        validators=[Optional(), URL(message="Неправильный URL")]
    )
    cover_image = FileField(
        "Обложка (jpg, png, gif)",
        validators=[Optional(), FileAllowed(['jpg','jpeg','png','gif'], 'Только изображения!')]
    )
    submit = SubmitField("Сохранить книгу")