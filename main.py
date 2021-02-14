from flask import Flask, jsonify, make_response
from flask_restful import Resource, Api, abort,request

app = Flask(__name__)
api = Api(app)

# Create app and api
books = {
    '1': {
        'isbn': '744586',
        'title': 'Cien años de soledad',
        'description': 'Lorem insup lol.',
        'autor': 'Gabriel Garcia Marquez'
    },
    '2': {
        'isbn': '7894546',
        'title': 'De animales a dioses',
        'description': 'Lorem insup lol.',
        'autor': 'Yuval Noah Harari'
    }
}


def abort_if_book_doesnot_exits(book_id):
    abort(404, message='El libro con id {} no existe'.format(book_id))

class BooksList(Resource):
    def get(self):
        return jsonify({'data': books})  # Returns as json in data variables


# Returns an specific id book
class Book(Resource):
    def get(self, book_id):
        if book_id not in books:
            abort_if_book_doesnot_exits(book_id)
        # Returns a response as json with some info code
        return make_response(jsonify(books[book_id]), 200)

class Authors(Resource):
    pass


class Generes(Resource):
    pass


api.add_resource(BooksList, '/books')
api.add_resource(Book, '/book/<book_id>')
api.add_resource(Authors, '/authors')
api.add_resource(Generes, '/generes')

if __name__ == '__main__':
    app.run(debug=True)
