import os

class Config:
    # Корень проекта
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev_key')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'instance', 'db.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Папка для загруженных обложек
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}