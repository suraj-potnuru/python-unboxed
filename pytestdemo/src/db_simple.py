class DatabaseClient:
    def insert_user(self, user_id, name):
        # Logic to connect to actual database and insert
        return True

def create_user(db_client, user_id, name):
    result = db_client.insert_user(user_id, name)
    # Bunch of statements that actually does soem use full stuff
    return result
