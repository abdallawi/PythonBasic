items = [
    ('Product1', 420),
    ('Product2', 20),
    ('product3', 102),
    ('product4', 1470),
    ('product5', 99),
    ('product6', 1),
    ('product7', 47),
    ('Product8', 55)
]

list_prices = [item[1] for item in items]
print(list_prices)

list_cheap_products = [item for item in items if item[1] < 100]
print(list_cheap_products)
