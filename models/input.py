class ProductInput:
    def __init__(self, product, qtd, nfe):
        self.product = product
        self.qtd = qtd
        self.nfe = nfe

    def __str__(self):
        return "Input of product with name {0}, with quantity of {2} in fiscal number: {3}".format(self.product.name,
                                                                                                   self.qtd, self.nfe)
