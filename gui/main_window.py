from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QAction


class MainWindowApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.toolbar = self.addToolBar('Opções')
        self.init_ui()

    def init_ui(self):
        product_action = QAction(QIcon('resources/icon/product.png'), 'Produto', self)
        input_action = QAction(QIcon('resources/icon/product_input.png'), 'Compra (Entrada)', self)
        output_action = QAction(QIcon('resources/icon/product_output.png'), 'Saída (Venda)', self)

        self.toolbar.addAction(product_action)
        self.toolbar.addAction(input_action)
        self.toolbar.addAction(output_action)

        exit_action = QAction(QIcon('resources/icon/exit.png'), 'Fechar', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Fechar')
        exit_action.triggered.connect(self.close)

        new_product = QAction(QIcon('resources/icon/add.png'), 'Novo', self)
        new_product.setStatusTip('Adicionar produto')
        search_product = QAction(QIcon('resources/icon/search.png'), 'Pesquisar', self)
        search_product.setStatusTip('Pesquisar produto')

        new_product_input = QAction(QIcon('resources/icon/add.png'), 'Novo', self)
        new_product_input.setStatusTip('Adicionar Compra')
        search_product_input = QAction(QIcon('resources/icon/search.png'), 'Pesquisar', self)
        search_product_input.setStatusTip('Pesquisar Compra')

        new_product_output = QAction(QIcon('resources/icon/add.png'), 'Novo', self)
        new_product_output.setStatusTip('Adicionar Venda')
        search_product_output = QAction(QIcon('resources/icon/search.png'), 'Pesquisar', self)
        search_product_output.setStatusTip('Pesquisar Venda')

        input_report = QAction("Compras", self)
        input_report.setStatusTip("Relatório de Compras")
        output_report = QAction("Vendas", self)
        output_report.setStatusTip("Relatório de Vendas")
        product_report = QAction("Produtos", self)
        product_report.setStatusTip("Relatório de Produtos")

        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False)

        file_menu = menu_bar.addMenu('&Arquivo')
        file_menu.addAction(exit_action)

        product_menu = menu_bar.addMenu('&Produtos')
        product_menu.addAction(new_product)
        product_menu.addAction(search_product)

        input_menu = menu_bar.addMenu('&Compras')
        input_menu.addAction(new_product_input)
        input_menu.addAction(search_product_input)

        output_menu = menu_bar.addMenu('&Vendas')
        output_menu.addAction(new_product_output)
        output_menu.addAction(search_product_output)

        report_menu = menu_bar.addMenu('&Relatório')
        report_menu.addAction(input_report)
        report_menu.addAction(output_report)
        report_menu.addAction(product_report)

        self.setWindowTitle('Inventory Manager - Controle de Estoque')
        self.showMaximized()
        self.show()

    def add_layout(self, view):
        self.current_view = view
