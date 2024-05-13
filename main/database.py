from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from urllib.parse import quote_plus

username = 'username'  # your MySQL username
password = quote_plus('NewPassword@1234')  # your MySQL password, URL-encoded
host = 'localhost'     # your MySQL host, localhost if running on the same machine
dbname = 'testdb'      # your database name

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{username}:{password}@{host}/{dbname}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, echo=True  # echo=True will log all the SQL generated
)

SessionLocal = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
