import argparse
from app import create_app, db
from app.models.user import User

app = create_app()
with app.app_context():
    parser = argparse.ArgumentParser()
    parser.add_argument("email")
    parser.add_argument("username")
    parser.add_argument("password")
    args = parser.parse_args()
    admin = User(email=args.email, username=args.username)
    admin.set_password(args.password)
    db.session.add(admin)
    db.session.commit()
    print("Admin created.")