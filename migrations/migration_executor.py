import sqlite3

from util.file_util import FileUtil


class MigrationExecutor:
    def start(self, database="inventory", directory="../resources/migration"):
        connection = sqlite3.connect(database)
        file_paths = FileUtil.get_file_paths_from_directory(directory)
        for file_path in file_paths:
            with open(file_path) as sql_file:
                for line in sql_file:
                    connection.execute(line)
                connection.commit()
                connection.close()
