from supplier import Supplier
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from order import Order
from bulk_discount import BulkDiscount
from percentage_discount import PercentageDiscount
from student_discount import StudentDiscount

supplier = Supplier("S001", "Tech Supplies Inc.", "sales@tech.com")

physical_product = PhysicalProduct("P001", "Laptop", 100.00, 10, 2.5, supplier)

digital_product = DigitalProduct("P002", "Software", 50.0, 20, 1000, supplier)

order = Order("O001", BulkDiscount(200,20))

order.add_order_line(physical_product, 2)

order.add_order_line(digital_product, 1)

print("Bulk Discount:")
print(order.calculate_total())

order.set_discount(PercentageDiscount(10))

print("Percentage Discount:")
print(order.calculate_total())

order.set_discount(StudentDiscount())

print("Student Discount:")
print(order.calculate_total())


from product_factory import ProductFactory
from supplier import Supplier


supplier = Supplier(
    "S001",
    "Tech Supplies",
    "sales@tech.com"
)


print("\n========== FACTORY TEST ==========")


physical_product = ProductFactory.create(
    product_type="physical",
    product_id="P001",
    name="Laptop",
    price=1200.0,
    stock_quantity=10,
    supplier=supplier,
    weight=2.5
)


digital_product = ProductFactory.create(
    product_type="digital",
    product_id="D001",
    name="Photo Editor",
    price=49.90,
    stock_quantity=100,
    supplier=supplier,
    download_size=500
)


physical_product.display_information()

print()

digital_product.display_information()

# ProductFactory.create(product_type="service", product_id="S001", name="Installation", price=30.0, stock_quantity=5, supplier=supplier)

print("\n========== VALIDATION TEST ==========")

try:
    invalid_product = ProductFactory.create(
        product_type="physical",
        product_id="P100",
        name="Invalid Product",
        price=-10.0,
        stock_quantity=5,
        supplier=supplier,
        weight=1.0
    )

except ValueError as error:
    print("Invalid price:", error)

try:
    invalid_product = ProductFactory.create(
        product_type="physical",
        product_id="P101",
        name="Invalid Stock Product",
        price=50.0,
        stock_quantity=-5,
        supplier=supplier,
        weight=1.0
    )

except ValueError as error:
    print("Invalid stock:", error)

try:
    order.add_order_line(physical_product, 0)

except ValueError as error:
    print("Invalid quantity:", error)

try:
    physical_product.update_stock(-10)

except ValueError as error:
    print("Invalid stock update:", error)