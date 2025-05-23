import os
from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf import CSRFProtect
from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()

def create_app():
    # Настраиваем instance-путь
    project_root = os.path.abspath(os.path.dirname(__file__) + '/../')
    instance_dir = os.path.join(project_root, 'instance')
    os.makedirs(instance_dir, exist_ok=True)

    # Создаем приложение с указанием instance_path
    app = Flask(
        __name__,
        instance_path=instance_dir,
        instance_relative_config=True
    )
    app.config.from_object(Config)

    # Инициализируем расширения
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    # Создаем папку для обложек, если нужно
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    # Отдача загруженных обложек
    @app.route('/uploads/<path:filename>')
    def uploaded_file(filename):
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

    # Регистрируем Blueprint-ы
    from app.routes.auth import auth_bp
    from app.routes.main import main_bp
    from app.api.routes import api_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp, url_prefix='/api')

    # Здесь — принудительное создание всех таблиц по моделям
    with app.app_context():
        db.create_all()

    return app