import csv

csv_file = './csv-files/own_csv_file.csv'

with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['transaction_id', 'product_id', 'price'])
    writer.writerow([1000, 1, 5])
    writer.writerow([1001, 2, 420])
    writer.writerow([1002, 1, 5])

with open('./csv-files/Columbus_Ed_astro_pi_datalog.csv') as file:
    reader = csv.reader(file)

    list_csv_content = list(reader)
    list_headers = list_csv_content.pop(0)

    for row in list_csv_content:
        for i in range(len(row)):
            print(f'{list_headers[i]} : {row[i]}')
    else:
        print()