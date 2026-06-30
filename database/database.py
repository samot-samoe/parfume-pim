from sqlalchemy import create_engine

DATABASE_URL = "postgresql+psycopg://pim_user:1234@localhost:5432/pim"

engine = create_engine(DATABASE_URL)