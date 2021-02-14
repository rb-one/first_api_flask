from flask import Flask, jsonify, make_response
from flask_restful import Resource, Api, abort, request

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
        # Returns as json in data variables
        return jsonify({'data': books})  

    def post(self):
        # Get the request as json format (type dict)
        json = request.get_json(force=True)
        # Create Index to post the new book
        index = len(books) + 1
        # Save the new book in the database
        books.update({str(index): json })
        # Return feedback to user
        return 'Libro agregado correctamente con ID: ' + str(index)


class Book(Resource):
    def get(self, book_id):
        if book_id not in books:
            abort_if_book_doesnot_exits(book_id)
        # Returns a response as json with some info code
        return make_response(jsonify(books[book_id]), 200)

    def put(self, book_id):
        if book_id not in books:
            abort_if_book_doesnot_exits(book_id)
        # Get the request as json format (type dict)
        json = request.get_json(force=True)
        # Update Dictionary/ Save the new book in the database
        books.update({str(book_id): json})
        # Return feedback to user
        return 'Se modificado correctamente el Libro con ID: ' + str(book_id)
    
    def delete(self, book_id):
        if book_id not in books:
            abort_if_book_doesnot_exits(book_id)
        # Removes element from Dictionary / database
        books.pop(book_id)
        return 'Se eliminado correctamente el Libro con ID: ' + str(book_id)


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
