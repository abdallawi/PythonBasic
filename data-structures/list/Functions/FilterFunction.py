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

cheap_product = list(filter(lambda cheap_item: cheap_item[1] < 100, items))
print(cheap_product)
