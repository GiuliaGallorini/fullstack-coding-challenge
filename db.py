from sqlalchemy import create_engine
from sqlalchemy import Table, Column, String, MetaData

DATABASE_URI = 'postgres://postgres:translate.19@localhost:5432/postgres'


def create_database():

    engine = create_engine(DATABASE_URI)

    meta = MetaData(engine)
    table_test = Table('table_test', meta,
                       Column('uid', String, primary_key=True),
                       Column('source_language', String),
                       Column('target_language', String),
                       Column('status', String),
                       Column('text', String),
                       Column('translatedText', String),
                       )

    # If table don't exist, Create.
    if not engine.dialect.has_table(engine, table_test):

        # Create
        table_test.create()

    return table_test


def save_into_database(data):

    table_test = create_database()

    engine = create_engine(DATABASE_URI)

    insert_statement = table_test.insert().values(uid=data['uid'], source_language=data['source_language'],
                                                  target_language=data['target_language'], status=data['status'], text=data['text'], translatedText=data['translatedText'])

    engine.connect().execute(insert_statement)


def read_database():
    table_test = create_database()

    engine = create_engine(DATABASE_URI)

    select_statement = table_test.select()
    result_set = engine.connect().execute(select_statement)

    res = []
    for r in result_set:
        res.append(r)

    return res
