from flask import request
from flask_restx import Resource, Namespace

from dao.model.feature import FeatureSchema
from implemented import feature_service

feature_ns = Namespace('movies')


@feature_ns.route('/')
class FeaturesView(Resource):
    def get(self):
        director = request.args.get("director_id")
        genre = request.args.get("genre_id")
        year = request.args.get("year")
        filters = dict(
            director_id = director,
            genre_id = genre,
            year = year,
        )
        all_features = feature_service.get_all(filters)
        response = FeatureSchema(many=True).dump(all_features)
        return response, 200

    def post(self):
        json_data = request.json
        feature = feature_service.create(json_data)
        return "", 201, {"location": f"/movies/{feature.id}"}


@feature_ns.route('/<int:fid>')
class FeatureView(Resource):
    def get(self, fid):
        ftr = feature_service.get_one(fid)
        data = FeatureSchema().dump(ftr)
        return data, 200

    def put(self, fid):
        json_data = request.json
        if 'id' not in json_data:
            json_data["id"] = fid
        feature_service.update(json_data)
        return "", 204

    def delete(self, fid):
        feature_service.delete(fid)
        return "", 204
