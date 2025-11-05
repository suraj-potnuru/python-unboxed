"""
This is the entry point to the chatbot api
"""
import os
from lib import DatabaseService

HOST_NAME = os.environ.get("HOST_NAME", "fallback.host.com")

if __name__ == "__main__":

    # initialize db service
    db_service = DatabaseService(host_name = HOST_NAME)
    db_service.connect_to_database()

    # db_service._conn.execute_query()
