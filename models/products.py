class Product:
    def __init__(self, name, description, bar_code, qtd):
        self.bar_code = bar_code
        self.name = name
        self.description = description
        self.qtd = qtd

    def __str__(self):
        return "Product with code {0} and name {1}".format(self.bar_code, self.name)
