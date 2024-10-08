from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

POSTGRES_DATABASE_URL = "sqlite:///./database.db"
#engine = create_engine(POSTGRES_DATABASE_URL,connect_args={"check_same_thread": False})
engine = create_engine(POSTGRES_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)

Base = declarative_base()

# def get_db():
#     with SessionLocal() as db:
#         yield db

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()