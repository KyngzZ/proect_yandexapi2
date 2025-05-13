from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from app.forms.book_forms import BookForm
from app.models.book import Book
from app import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@login_required
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)

@main_bp.route('/add_book', methods=['GET','POST'])
@login_required
def add_book():
    form = BookForm()
    if form.validate_on_submit():
        book = Book(title=form.title.data, author=form.author.data,
                    genre=form.genre.data, condition=form.condition.data,
                    description=form.description.data, user_id=current_user.id)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('add_book.html', form=form)