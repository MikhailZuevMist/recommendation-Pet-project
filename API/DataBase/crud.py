from sqlalchemy import text
from . import db as database


class Parent:
    table_name = None
    db = database.get_engine()

    def __init__(self, title):
        self.title = title

    def get_item_by_title(self):
        self.validate()
        dct = {}
        with self.db.connect() as conn:
            query = f"SELECT * FROM {self.table_name} WHERE title = '{self.title}';"
            result = conn.execute(text(query))
            for i in result:
                for j,jj in zip(['title', 'score', "date", 'summary', 'Atmosphere', 'Tags', 'RecommendationsGame', 'RecommendationsBook'],i):
                    dct.update({j: jj})
                return dct

    def list_of_items(self):
        with self.db.connect() as conn:
            query = f"SELECT * FROM {self.table_name};"
            result = conn.execute(text(query))
            lst = [i for i in result]
            return lst




    def validate(self):
        with self.db.connect() as conn:
            query = f"SELECT COUNT(*) FROM {self.table_name} WHERE title = '{self.title}';"
            result = conn.execute(text(query))
            for i in result:
                if i[0] > 1:
                    raise ValueError('Результатов больше чем один')
                if i[0] == 0:
                    raise ValueError('Такого фильма нет в БД')




class Movies(Parent):
    table_name = 'movies'


# movie = Movies('Tokyo Story')
# print(movie.get_item_by_title())
