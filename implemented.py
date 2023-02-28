from setup_db import db
from dao.feature import FeatureDAO
from service.feature import FeatureService
from dao.director import DirectorDAO
from dao.genre import GenreDAO

director_dao = DirectorDAO(session=db.session)
genre_dao = GenreDAO(session=db.session)
feature_dao = FeatureDAO(session=db.session)

# director_service = DirectorService(dao=director_dao)
# genre_service = GenreService(dao=genre_dao)
feature_service = FeatureService(dao=feature_dao)