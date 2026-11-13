from product import Product
from order_line import OrderLine
from discount_strategy import DiscountStrategy
from no_discount import NoDiscount

class Order:
    def __init__(self, order_id: str, discount: DiscountStrategy | None = None) -> None:
        self.__order_id: str = order_id
        self.__order_lines: list[OrderLine] = []

        if discount is None:
            self.__discount: DiscountStrategy = NoDiscount()
        else:
            self.__discount = discount

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.__order_lines.append(order_line)

    def set_discount(self, discount: DiscountStrategy) -> None:
        self.__discount = discount

    def calculate_total(self) -> float:
        total = 0.0
        
        for order_line in self.__order_lines:
            total += order_line.calculate_subtotal()

        return self.__discount.apply(total)

    def display_order(self) -> None:
        print(f"Order ID: {self.__order_id}")
        print("--------------------------------------------")

        for order_line in self.__order_lines:
            order_line.display_information()

        print("--------------------------------------------")
        print(f"Total after discount: ${self.calculate_total():.2f}")

    def get_order_lines(self) -> list[OrderLine]:
        return list(self.__order_lines)