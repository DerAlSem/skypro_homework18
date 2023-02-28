from dao.feature import FeatureDAO


class FeatureService:
    def __init__(self, dao: FeatureDAO):
        self.ftr_dao = dao

    def get_one(self, fid):
        return self.ftr_dao.get_one(fid)

    def get_all(self, filters):
        if filters['director_id']:
            movies = self.ftr_dao.get_by_director_id(filters['director_id'])
        elif filters['genre_id']:
            movies = self.ftr_dao.get_by_genre_id(filters['genre_id'])
        elif filters['year']:
            movies = self.ftr_dao.get_by_year(filters['year'])
        else:
            movies = self.ftr_dao.get_all()
        return movies

    def create(self, data):
        return self.ftr_dao.create(data)

    def update(self, data):
        self.ftr_dao.update(data)
        return self.ftr_dao

    def delete(self, fid):
        self.ftr_dao.delete(fid)