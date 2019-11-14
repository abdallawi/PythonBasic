products = ['Xiaomi Mi Electric Pro Scooter',
            'AMD Ryzen 7 3700X socket AM4 processor',
            'Bowers & Wilkins PX5 hoofdtelefoon',
            'Blue Microphones Yeti USB microfoon',
            ]

prices = [549, 359, 299, 129, 253 , 255]

list_combined = list(zip(products, prices, 'ABCDERHGF'))

print(list_combined)

list_combined = list(zip(list_combined, range(10)))
print(list_combined)

