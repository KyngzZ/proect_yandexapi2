import os
import uuid
from flask import Blueprint, render_template, redirect, url_for, current_app, flash
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename

from app.forms.book_forms import BookForm
from app.models.book import Book
from app import db

main_bp = Blueprint("main", __name__)

def allowed_file(filename):
    ext = filename.rsplit('.', 1)[-1].lower()
    return '.' in filename and ext in current_app.config['ALLOWED_EXTENSIONS']

@main_bp.route("/", methods=["GET"])
@login_required
def index():
    books = Book.query.order_by(Book.added_at.desc()).all()
    return render_template("index.html", books=books)

@main_bp.route("/add_book", methods=["GET", "POST"])
@login_required
def add_book():
    form = BookForm()
    if form.validate_on_submit():
        filename = None
        filedata = form.cover_image.data
        if filedata:
            if allowed_file(filedata.filename):
                # Генерируем уникальное имя
                ext = filedata.filename.rsplit('.', 1)[1].lower()
                filename = secure_filename(f"{uuid.uuid4().hex}.{ext}")
                filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
                filedata.save(filepath)
            else:
                flash("Неподдерживаемый формат обложки.")
                return render_template("add_book.html", form=form)

        book = Book(
            title=form.title.data,
            author=form.author.data,
            genre=form.genre.data,
            condition=form.condition.data,
            description=form.description.data,
            link=form.link.data,
            cover_image=filename,
            user_id=current_user.id
        )
        db.session.add(book)
        db.session.commit()
        return redirect(url_for("main.index"))

    return render_template("add_book.html", form=form)