from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from implemented import genre_dao

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = genre_dao.get_all()
        data = GenreSchema(many=True).dump(genres)
        return data, 200


@genre_ns.route('/<int:rid>')
class GenreView(Resource):
    def get(self, rid):
        r = genre_dao.get_one(rid)
        sm_d = GenreSchema().dump(r)
        return sm_d, 200
