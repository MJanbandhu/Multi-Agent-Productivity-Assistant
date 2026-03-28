from db.queries import execute_query

def add_note(content):
    query = "INSERT INTO notes (content) VALUES (%s);"
    execute_query(query, (content,))
    return "Note added"

def get_notes():
    query = "SELECT * FROM notes;"
    return execute_query(query)