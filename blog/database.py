from click import echo
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DB_URL = 'sqlite:///./blog_db.db'
engine = create_engine(
    SQLALCHEMY_DB_URL, connect_args={"check_same_thread": False})
    # connect_args 부분은 sqlite 쓸 때만 필요한 부분

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


