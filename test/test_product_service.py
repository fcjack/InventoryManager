import os
import sqlite3
import unittest

from migrations.migration_executor import MigrationExecutor
from services.product_service import ProductService

from models.products import Product


class ProductServiceTest(unittest.TestCase):
    def setUp(self):
        self.product_service = ProductService()
        migration = MigrationExecutor()
        migration.start()

    def test_add_product(self):
        product = Product("test", "product test", "12311231256", 10)
        self.product_service.add(product)
        conn = sqlite3.connect("inventory")
        cursor = conn.execute("SELECT * FROM product WHERE name = ?", [product.name])
        db_object = cursor.fetchone()
        conn.close()
        self.assertEqual(db_object[1], product.name)
        self.assertEqual(db_object[2], product.description)
        self.assertEqual(db_object[3], product.bar_code)
        self.assertEqual(db_object[4], product.qtd)

    def test_list_products(self):
        product = Product("test", "product test", "12311231256", 10)
        self.product_service.add(product)
        result = self.product_service.list()
        self.assertEqual(1, len(result))

    def tearDown(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        os.remove(os.path.join(my_path, "inventory"))


if __name__ == '__main__':
    unittest.main()
