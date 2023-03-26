from sqlalchemy import text, MetaData, Table, create_engine
import copy
postgresql = {'pguser': 'postgres',
              'pgpassword': 'Blade007',
              'pghost': 'localhost',
              'pgport': 5432,
              'pgdb': 'Cross_Worlds_Bot'
              }


def get_engine(user=postgresql['pguser'], password=postgresql['pgpassword'], host=postgresql['pghost'],
               port=postgresql['pgport'], db=postgresql['pgdb']):
    url = f"postgresql://{user}:{password}@{host}:{port}/{db}"
    db = create_engine(url)
    return db
engine = get_engine()
metadata = MetaData()
with engine.connect() as conn:
# create a SQLAlchemy table object for the table you want to query
    table = Table('movies', metadata,  autoload_with=engine)
    print(table)
    # execute the query and return the results as a list of dictionaries
    results = conn.execute(table.select()).fetchall()
    dict = {}
    dict2 = {}
    for i in results:
        for ii, iii in zip(['title', 'score', "date", 'summary', 'GPT_answer', 'Atmosphere', 'Tags', 'RecommendationsGame', 'RecommendationsBook'],i):
            dict.update({ii: iii})
        dict2.update({i[9]: copy.deepcopy(dict)})
    print(dict2.get(5))



