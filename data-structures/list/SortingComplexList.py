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

items.sort()
print(items)

def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)