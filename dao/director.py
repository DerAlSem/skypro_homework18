from dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, did):
        return Director.query.get(did)

    def get_all(self):
        return Director.query.all()

    def create(self, data):
        director = Director(**data)
        self.session.add(director)
        self.session.commit()
        return director

    def delete(self, did):
        director = self.get_one(did)
        self.session.delete(director)
        self.session.commit()

    def update(self, data):
        director = self.get_one(data.get("id"))
        director.name = data.get("name")

        self.session.add(director)
        self.session.commit()
