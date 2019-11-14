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

# prices = []
#
# for item in items:
#     prices.append(item[1])
map_only_prices = list(map(lambda single_item: single_item[1], items))

print(map_only_prices)








