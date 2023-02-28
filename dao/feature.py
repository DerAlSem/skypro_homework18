from dao.model.feature import Feature


class FeatureDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, fid):
        return Feature.query.get(fid)

    def get_all(self):
        return Feature.query.all()

    def get_by_director_id(self, did):
        return Feature.query.filter(Feature.director_id == did).all()

    def get_by_genre_id(self, gid):
        return Feature.query.filter(Feature.genre_id == gid).all()

    def get_by_year(self, yid):
        return Feature.query.filter(Feature.year == yid).all()

    def create(self, data):
        feature = Feature(**data)
        self.session.add(feature)
        self.session.commit()
        return feature

    def delete(self, fid):
        feature = self.get_one(fid)
        self.session.delete(feature)
        self.session.commit()

    def update(self, data):
        feature = self.get_one(data.get("id"))
        feature.name = data.get("name")

        self.session.add(feature)
        self.session.commit()
