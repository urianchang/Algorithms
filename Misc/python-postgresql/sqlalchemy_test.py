from sqlalchemy import (
    create_engine,
    Column,
    ForeignKey,
    Integer,
    MetaData,
    String,
    Table,
)
from sqlalchemy_utils import database_exists, create_database

def connect(user, password, db, host='localhost', port=5432):
    '''Returns a connection and a metadata object'''
    # Connect with PostgreSQL URL
    if password:
        url = "postgresql://{}:{}@{}:{}/{}"
        url = url.format(user, password, host, port, db)
    else:
        url = "postgresql://{}@{}:{}/{}".format(user, host, port, db)

    # create_engine() returns a connection object
    con = create_engine(url, client_encoding='utf8')

    # Check if database exists. If not, create it.
    if not database_exists(con.url):
        create_database(engine.url)

    # bind connection to MetaData()
    meta = MetaData(bind=con, reflect=True)

    return con, meta

con, meta = connect('urian', None, 'tennis')

"""
# Create tables
slams = Table('slams', meta,
    Column('name', String, primary_key=True),
    Column('country', String)
)

results = Table('results', meta,
    Column('slam', String, ForeignKey('slams.name')),
    Column('year', Integer),
    Column('result', String)
)

meta.create_all(con)
"""

"""
# Get all created tables from MetaData
for table in meta.tables:
    print table
"""

"""
# Inserting records
slams_table = meta.tables['slams']
request = slams_table.insert().values(name="Wimbledon", country="United Kingdom")
result = con.execute(request)
"""

"""
# Inserting multiple records
victories = [
    {'slam': 'Wimbledon', 'year': 2003, 'result': 'W'},
    {'slam': 'Wimbledon', 'year': 2004, 'result': 'W'},
    {'slam': 'Wimbledon', 'year': 2005, 'result': 'W'}
]
con.execute(meta.tables['results'].insert(), victories)
"""

"""
# Getting all columns from a table
results_table = meta.tables['results']
for col in results_table.c:
    print col
"""

# Selecting
results = meta.tables['results']
# for row in con.execute(results.select()):
#     print row

request = results.select().where(results.c.year == 2005)
for row in con.execute(request):
    print row
