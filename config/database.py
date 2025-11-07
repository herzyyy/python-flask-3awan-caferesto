from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import psycopg  # <-- penting: ini psycopg v3, bukan psycopg2
from sqlalchemy.dialects import registry

# Daftarkan psycopg (v3) sebagai driver default PostgreSQL
registry.register("postgresql", "sqlalchemy.dialects.postgresql.psycopg", "PGDialect_psycopg")

# URL koneksi TANPA '+psycopg'
DATABASE_URL = "postgresql://postgres:gfKyzmlBiEmNqlUXxjKFiIbdTJSZfLdN@shortline.proxy.rlwy.net:58270/railway"
# Engine koneksi
engine = create_engine(DATABASE_URL, echo=True)

# Session untuk query
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base untuk model ORM
Base = declarative_base()

# Dependency untuk session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
