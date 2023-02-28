from flask_restx import Resource, Namespace

from dao.model.director import DirectorSchema
from implemented import director_dao

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors = director_dao.get_all()
        data = DirectorSchema(many=True).dump(directors)
        return data, 200


@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        director = director_dao.get_one(did)
        data = DirectorSchema().dump(director)
        return data, 200
