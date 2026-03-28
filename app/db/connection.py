import psycopg2

def get_connection():
    conn = psycopg2.connect(
        host="YOUR_HOST",
        database="postgres",
        user="postgres",
        password="YOUR_PASSWORD",
        port="5432"
    )
    return conn