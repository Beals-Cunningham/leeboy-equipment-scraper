import mysql.connector, os
from dotenv import load_dotenv


def box(data):
    load_dotenv(os.path.join(os.getcwd(), '.env'))
    try:
        with mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            username=os.getenv("DB_USERNAME"),
            port=os.getenv("DB_PORT"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_DATABASE")
        ) as connection:
            print("Connected to MySQL database")
            cursor = connection.cursor()
            unpack(data, cursor)
    except:
        print("Error connecting to MySQL database")


def unpack(data, c):
    existing_rows = c.execute("SELECT * FROM takeout")
    