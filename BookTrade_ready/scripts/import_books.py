import argparse, json
from app import create_app, db
from app.models.book import Book

app = create_app()
with app.app_context():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="Path to JSON file")
    args = parser.parse_args()
    data = json.load(open(args.file))
    for item in data:
        db.session.add(Book(**item))
    db.session.commit()
    print("Books imported.")