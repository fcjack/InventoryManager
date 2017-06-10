from database.generic_repository import GenericRepository
from models.products import Product


class ProductRepository(GenericRepository):
    def list(self):
        connection = self.get_connection()
        cur = connection.execute("SELECT * FROM product")
        result = cur.fetchall()
        products = []
        for product in result:
            products.append(Product(product[0], product[1], product[2], product[3]))
        return products

    def add(self, product):
        connection = self.get_connection()
        connection.execute(
            "INSERT INTO product VALUES ({0}, {1}, {2}, {3})".format(product.name, product.description,
                                                                     product.bar_code, product.qtd))
        connection.commit()
        connection.close()

    def update(self, product):
        connection = self.get_connection()
        connection.execute(
            "UPDATE product set description = {1}, bar_code={2}, qtd = {3} WHERE name = {0}".format(product.name,
                                                                                                    product.description,
                                                                                                    product.bar_code,
                                                                                                    product.qtd))
        connection.commit()
        connection.close()

    def remove(self, product_name):
        connection = self.get_connection()
        connection.execute("DELETE FROM product WHERE name = {0}".format(product_name))
        connection.commit()
        connection.close()
