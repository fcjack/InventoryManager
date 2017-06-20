import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction

from migrations.migration_executor import MigrationExecutor


def run(name, code):
    pass


class MainWindowApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        product_action = QAction(QIcon('resources/icon/product.png'), 'Produto', self)
        input_action = QAction(QIcon('resources/icon/product_input.png'), 'Compra (Entrada)', self)
        output_action = QAction(QIcon('resources/icon/product_output.png'), 'Saída (Venda)', self)

        self.toolbar = self.addToolBar('Opções')
        self.toolbar.addAction(product_action)
        self.toolbar.addAction(input_action)
        self.toolbar.addAction(output_action)

        exit_action = QAction(QIcon('resources/icon/exit.png'), 'Fechar', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Fechar')
        exit_action.triggered.connect(self.close)

        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)
        file_menu = menu_bar.addMenu('&Arquivo')
        product_menu = menu_bar.addMenu('&Produtos')
        input_menu = menu_bar.addMenu('&Compras')
        output_menu = menu_bar.addMenu('&Vendas')
        file_menu.addAction(exit_action)

        self.setWindowTitle('Inventory Manager - Controle de Estoque')
        self.showMaximized()
        self.show()


if __name__ == '__main__':
    migration = MigrationExecutor()
    migration.start()

    app = QApplication(sys.argv)
    ex = MainWindowApp()
    sys.exit(app.exec_())
