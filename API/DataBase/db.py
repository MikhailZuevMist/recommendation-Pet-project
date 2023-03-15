from sqlalchemy import create_engine
from .Settings import postgresql as settings


def get_engine(user=settings['pguser'], password=settings['pgpassword'], host=settings['pghost'],
               port=settings['pgport'], db=settings['pgdb']):
    url = f"postgresql://{user}:{password}@{host}:{port}/{db}"
    db = create_engine(url)
    return db


# def get_list(db):
#     with db.connect() as conn:
#         query = "SELECT title FROM movies;"
#         result = conn.execute(text(query))
#         for i in result:
#             print(i[0])
#
#
# db = get_engine()
# get_list(db)