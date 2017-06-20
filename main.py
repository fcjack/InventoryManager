import sys

from PyQt5.QtWidgets import QApplication

from gui.main_window import MainWindowApp
from migrations.migration_executor import MigrationExecutor

if __name__ == '__main__':
    migration = MigrationExecutor()
    migration.start()

    app = QApplication(sys.argv)
    ex = MainWindowApp()
    sys.exit(app.exec_())
