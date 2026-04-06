from app.db.queries import execute_query

def create_task(title):
    query = "INSERT INTO tasks (title, status) VALUES (%s, 'pending');"
    execute_query(query, (title,))
    return "Task created successfully"

def get_tasks():
    query = "SELECT * FROM tasks;"
    return execute_query(query)