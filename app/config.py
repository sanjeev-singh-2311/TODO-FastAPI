from starlette.config import Config

config = Config('.env')

POSTGRES_URL = f"postgresql://{config.get('POSTGRES_USER')}:{config.get('POSTGRES_PASSWORD')}@{config.get('POSTGRES_HOST')}:5432/{config.get('POSTGRES_DB')}"

