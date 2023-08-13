from sqlalchemy import create_engine, MetaData

DATABASE_URL = "postgresql://postgres:1bigone@localhost:5432/test_postgresDB"
CACHE_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL)
cache_engine = create_engine(CACHE_DATABASE_URL)
