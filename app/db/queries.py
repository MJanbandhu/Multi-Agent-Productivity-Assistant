import psycopg2
import os

def get_connection():
    try:
        return psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT"),
            sslmode="require"
        )
    except Exception as e:
        print("DB CONNECTION ERROR:", e)
        return None   # IMPORTANT: don't crash


def execute_query(query, params=None):
    conn = get_connection()

    if conn is None:
        return "Database connection failed"

    try:
        cursor = conn.cursor()
        cursor.execute(query, params)

        if query.strip().lower().startswith("select"):
            result = cursor.fetchall()
        else:
            conn.commit()
            result = "Success"

        cursor.close()
        conn.close()
        return result

    except Exception as e:
        print("DB QUERY ERROR:", e)
        return f"Query error: {str(e)}"