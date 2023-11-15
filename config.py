import os

DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')

DB_CONNECTION_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}'
print(DB_CONNECTION_URL)
