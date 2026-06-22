import psycopg2

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="scraper_db",
        user="postgres",
        password="brinda2005"
    )