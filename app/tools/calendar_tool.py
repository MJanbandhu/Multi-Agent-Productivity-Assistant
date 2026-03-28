from db.queries import execute_query

def create_event(title, time):
    query = "INSERT INTO events (title, event_time) VALUES (%s, %s);"
    execute_query(query, (title, time))
    return "Event scheduled"

def get_events():
    query = "SELECT * FROM events;"
    return execute_query(query)