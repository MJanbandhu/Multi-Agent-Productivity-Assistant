from db.connection import get_connection

def execute_query(query, params=None):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(query, params)
    
    try:
        result = cursor.fetchall()
    except:
        result = None

    conn.commit()
    cursor.close()
    conn.close()

    return result