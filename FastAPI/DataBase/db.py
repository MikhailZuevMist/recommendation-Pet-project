from sqlalchemy import create_engine
from Settings import postgresql as settings
from sqlalchemy import text


def get_engine(user, password, host, port, db):
    url = f"postgresql://{user}:{password}@{host}:{port}/{db}"
    db = create_engine(url)
    return db


db = get_engine(settings['pguser'], settings['pgpassword'], settings['pghost'], settings['pgport'],
                'The Movies Dataset')


def get_list(db):
    with db.connect() as conn:
        query = "SELECT title FROM movies;"
        result = conn.execute(text(query))
        for i in result:
            print(i[0])


print(get_list(db))