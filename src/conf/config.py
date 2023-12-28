import os

from dotenv import dotenv_values

config = dotenv_values(".env")

DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
if all([DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME]) is False:
    DB_USER = config.get("DB_USER")
    DB_PASSWORD = config.get("DB_PASSWORD")
    DB_HOST = config.get("DB_HOST")
    DB_PORT = config.get("DB_PORT")
    DB_NAME = config.get("DB_NAME")


class Config:
    DB_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


config = Config
print(config.DB_URL)
