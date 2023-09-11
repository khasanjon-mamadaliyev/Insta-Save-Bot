from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str('BOT_TOKEN')
ADMINS = env.list('ADMINS')
IP = env.str('IP')
BOT_USERNAME = env.str('BOT_USERNAME')

POSTGRES_USER = env.str('POSTGRES_USER')
POSTGRES_PASSWORD = env.str('POSTGRES_PASSWORD')
POSTGRES_HOST = env.str('POSTGRES_HOST')
POSTGRES_PORT = env.str('POSTGRES_PORT')
POSTGRES_DB = env.str('POSTGRES_DB')

POSTGRESQL_URL = f'{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}'
DATABASE_URL = "postgresql+asyncpg://" + POSTGRESQL_URL
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://" + POSTGRESQL_URL
