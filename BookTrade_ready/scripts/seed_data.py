from app import create_app, db
from app.models.book import Book
app = create_app()
with app.app_context():
    if Book.query.first():
        print("Data already seeded.")
    else:
        sample = [
            {"title":"1984","author":"Джордж Оруэлл","genre":"Антиутопия","condition":"new","description":"Классика антиутопии."},
            {"title":"Мастер и Маргарита","author":"Михаил Булгаков","genre":"Роман","condition":"used","description":"Великая русская классика."},
            {"title":"Преступление и наказание","author":"Фёдор Достоевский","genre":"Роман","condition":"used","description":"Психологический роман."}
        ]
        for b in sample:
            db.session.add(Book(**b))
        db.session.commit()
        print("Initial books seeded.")