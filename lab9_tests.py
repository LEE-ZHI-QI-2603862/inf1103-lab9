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
