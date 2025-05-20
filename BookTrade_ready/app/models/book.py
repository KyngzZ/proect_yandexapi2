from app import db
from datetime import datetime

class Book(db.Model):
    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50))
    condition = db.Column(db.String(50))        # "new" или "used"
    description = db.Column(db.Text)
    link = db.Column(db.String(255))            # URL на онлайн-версию
    cover_image = db.Column(db.String(255))     # имя файла обложки
    added_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
