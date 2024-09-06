from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.load_settings import read_settings

DATABASE_URL = read_settings("database_url", "database", "postgresql")

# SQLAlchemy 연결, 세션, Base 클래스 생성
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# DB 세션 생성 (제너레이터)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
