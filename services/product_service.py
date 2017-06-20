from database import ProductRepository


class ProductService:
    def __init__(self):
        self.product_repository = ProductRepository()

    def list(self):
        return self.product_repository.list()

    def add(self, product):
        self.product_repository.add(product)

    def update(self, product):
        self.product_repository.update(product)

    def remove(self, product):
        self.product_repository.remove(product.name)
