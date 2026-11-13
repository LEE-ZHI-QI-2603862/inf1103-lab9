import unittest

from supplier import Supplier
from inventory import Inventory
from order import Order

from product_factory import ProductFactory

from no_discount import NoDiscount
from percentage_discount import PercentageDiscount
from bulk_discount import BulkDiscount
from student_discount import StudentDiscount

from product_loader import load_products


class TestLab9(unittest.TestCase):

    def setUp(self):
        self.supplier = Supplier(
            "S001",
            "Tech Supplies",
            "sales@tech.com"
        )

        self.physical_product = ProductFactory.create(
            product_type="physical",
            product_id="P001",
            name="Laptop",
            price=100.0,
            stock_quantity=10,
            supplier=self.supplier,
            weight=2.5
        )

        self.digital_product = ProductFactory.create(
            product_type="digital",
            product_id="D001",
            name="Software",
            price=50.0,
            stock_quantity=20,
            supplier=self.supplier,
            download_size=500
        )
    def test_no_discount(self):
        order = Order(
            "O001",
            NoDiscount()
        )

        order.add_order_line(
            self.physical_product,
            2
        )

        self.assertEqual(
            order.calculate_total(),
            200.0
        )
    def test_no_discount(self):
        order = Order(
            "O001",
            NoDiscount()
        )

        order.add_order_line(
            self.physical_product,
            2
        )

        self.assertEqual(
            order.calculate_total(),
            200.0
        )
    def test_percentage_discount(self):
        order = Order(
            "O002",
            PercentageDiscount(10)
        )

        order.add_order_line(
            self.physical_product,
            2
        )

        self.assertEqual(
            order.calculate_total(),
            180.0
        )

    def test_bulk_discount(self):
        order = Order(
            "O003",
            BulkDiscount(200, 20)
        )

        order.add_order_line(
            self.physical_product,
            2
        )

        self.assertEqual(
            order.calculate_total(),
            180.0
        )
    def test_student_discount(self):
        order = Order(
            "O004",
            StudentDiscount()
        )

        order.add_order_line(
            self.physical_product,
            2
        )

        self.assertEqual(
            order.calculate_total(),
            190.0
        )
    def test_change_discount(self):
        order = Order(
            "O005",
            NoDiscount()
        )

        order.add_order_line(
            self.physical_product,
            2
        )

        self.assertEqual(
            order.calculate_total(),
            200.0
        )

        order.set_discount(
            PercentageDiscount(10)
        )

        self.assertEqual(
            order.calculate_total(),
            180.0
        )
    def test_factory_creates_physical_product(self):
        product = ProductFactory.create(
            product_type="physical",
            product_id="P002",
            name="Mouse",
            price=25.0,
            stock_quantity=10,
            supplier=self.supplier,
            weight=0.2
        )

        self.assertEqual(
            product.get_name(),
            "Mouse"
        )
    def test_factory_creates_digital_product(self):
        product = ProductFactory.create(
            product_type="digital",
            product_id="D002",
            name="Photo Editor",
            price=49.90,
            stock_quantity=100,
            supplier=self.supplier,
            download_size=500
        )

        self.assertEqual(
            product.get_name(),
            "Photo Editor"
        )

    def test_unknown_product_type(self):
        with self.assertRaises(ValueError):

            ProductFactory.create(
                product_type="service",
                product_id="S001",
                name="Installation",
                price=30.0,
                stock_quantity=5,
                supplier=self.supplier
            )

    def test_invalid_price(self):
        with self.assertRaises(ValueError):

            ProductFactory.create(
                product_type="physical",
                product_id="P003",
                name="Bad Product",
                price=-10.0,
                stock_quantity=5,
                supplier=self.supplier,
                weight=1.0
            )

    def test_invalid_stock(self):
        with self.assertRaises(ValueError):

            ProductFactory.create(
                product_type="physical",
                product_id="P004",
                name="Bad Stock",
                price=50.0,
                stock_quantity=-2,
                supplier=self.supplier,
                weight=1.0
            )

    def test_invalid_order_quantity(self):
        order = Order("O006")

        with self.assertRaises(ValueError):

            order.add_order_line(
                self.physical_product,
                0
            )

    if __name__ == "__main__":
        unittest.main()