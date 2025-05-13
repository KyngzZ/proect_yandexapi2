from flask_restful import Resource, Api
from flask import Blueprint, request
from app.models.book import Book
from app import db

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

class BookList(Resource):
    def get(self):
        books = Book.query.all()
        return [{'id':b.id,'title':b.title,'author':b.author} for b in books]
    def post(self):
        data = request.get_json()
        book = Book(**data)
        db.session.add(book)
        db.session.commit()
        return {'message':'Book added'},201

api.add_resource(BookList, '/books')