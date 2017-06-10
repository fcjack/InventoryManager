import sqlite3


class GenericRepository:
    def get_connection(self):
        connection = sqlite3.connect('inventory')
        return connection
