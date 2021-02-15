from flask import Flask
from flask_restful import Api
from resources.books import Book, BooksList
from resources.authors import Authors
from resources.genres import Generes
from common.auth import generate_hash

app = Flask(__name__)
api = Api(app)

api.add_resource(BooksList, '/books')
api.add_resource(Book, '/book/<book_id>')
api.add_resource(Authors, '/authors')
api.add_resource(Generes, '/generes')
hash_api = generate_hash()
print(hash_api)


if __name__ == '__main__':
    app.run(debug=True)
