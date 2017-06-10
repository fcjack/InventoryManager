from database.generic_repository import GenericRepository
from models.products import Product


class ProductRepository(GenericRepository):
    def list(self):
        connection = self.get_connection()
        cur = connection.execute("SELECT * FROM product")
        result = cur.fetchall()
        products = []
        for product in result:
            products.append(Product(_id=product[0], name=product[1],
                                    description=product[2],
                                    bar_code=product[3],
                                    qtd=product[4]))
        return products

    def add(self, product):
        connection = self.get_connection()
        connection.execute(
            "INSERT INTO product(name, description, bar_code, qtd) "
            "VALUES (?, ?, ?, ?)",
            [product.name, product.description, product.bar_code, product.qtd])
        connection.commit()
        connection.close()

    def update(self, product):
        connection = self.get_connection()
        connection.execute(
            "UPDATE product SET name=?, description = ?, bar_code=?, qtd = ? WHERE id = ?", [product.name,
                                                                                             product.description,
                                                                                             product.bar_code,
                                                                                             product.qtd, product.id])
        connection.commit()
        connection.close()

    def remove(self, product_id):
        connection = self.get_connection()
        connection.execute("DELETE FROM product WHERE id = ?", [product_id])
        connection.commit()
        connection.close()
