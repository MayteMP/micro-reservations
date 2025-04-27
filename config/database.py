from sqlalchemy import create_engine
from dotenv import load_dotenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# La URL de conexión puede estar en las variables de entorno
ENV = os.getenv("ENV", "dev")
env_file = ".env.test" if ENV == "test" else ".env"
load_dotenv(env_file)
DATABASE_URL = os.getenv("DATABASE_URL")

# Crear la base de datos (Base) y metadata
Base = declarative_base()

# Configuración de la conexión
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {})

# Crear una sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
