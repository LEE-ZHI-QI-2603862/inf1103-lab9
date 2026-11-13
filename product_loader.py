import csv

from inventory import Inventory
from supplier import Supplier
from product_factory import ProductFactory


def load_products(
    path: str,
    inventory: Inventory,
    supplier: Supplier
) -> None:

    try:
        file = open(path, newline="")

    except FileNotFoundError:
        print(f"Products file not found: {path}")

    else:
        loaded = 0

        with file:
            reader = csv.DictReader(file)

            for row in reader:

                try:
                    product_type = row["product_type"]

                    price = float(row["price"])
                    stock = int(row["stock_quantity"])

                    if product_type == "physical":
                        product = ProductFactory.create(
                            product_type="physical",
                            product_id=row["product_id"],
                            name=row["name"],
                            price=price,
                            stock_quantity=stock,
                            supplier=supplier,
                            weight=float(row["weight"])
                        )

                    elif product_type == "digital":
                        product = ProductFactory.create(
                            product_type="digital",
                            product_id=row["product_id"],
                            name=row["name"],
                            price=price,
                            stock_quantity=stock,
                            supplier=supplier,
                            download_size=float(
                                row["download_size"]
                            )
                        )

                    else:
                        product = ProductFactory.create(
                            product_type=product_type,
                            product_id=row["product_id"],
                            name=row["name"],
                            price=price,
                            stock_quantity=stock,
                            supplier=supplier
                        )

                    inventory.add_product(product)
                    loaded += 1

                except ValueError as error:
                    print(
                        f"Skipping product "
                        f"{row['product_id']}: {error}"
                    )

        print(f"{loaded} products loaded.")

    finally:
        print("Load attempt finished.")