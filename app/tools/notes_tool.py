from app.db.queries import execute_query

def create_note(content):
    query = "INSERT INTO notes (content) VALUES (%s);"
    execute_query(query, (content,))
    return "Note created successfully"

def get_notes():
    query = "SELECT * FROM notes;"
    return execute_query(query)



def create_notes(title):
    return "Notes created (mock)"

def get_notes():
    return []