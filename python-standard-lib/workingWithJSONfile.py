import json
from pathlib import Path

mov_id = 'id'
title = 'title'
rel_year = 'release year'
json_file = Path('./json-files/movies.json')
json_file_nottingham = Path('./json-files/opendatanottingham.json')
new_line = "\n"
pount_sign = '\u00a3'
key_amount_paid = "Amount_Paid(Â£)"

movies = [
    {mov_id: 1, title: 'lucy', rel_year: 2014},
    {mov_id: 2, title: 'Interstellar', rel_year: 2014},
    {mov_id: 3, title: 'Transendence', rel_year: 2014},
    {mov_id: 4, title: 'Inception', rel_year: 2014},
    {mov_id: 5, title: 'Shutter island', rel_year: 2014},
]

print(type(movies), movies)

data = json.dumps(movies)
print(type(data), data)
json_file.write_text(data)

data = json_file_nottingham.read_text()

fines = json.loads(data)

for fine in fines:
    print(f'Offense: {fine.get("Contravention_Description")}{new_line}'
          f'Amount of fine: {fine[key_amount_paid]} {new_line}'
          f'Status : {fine.get("Status")}{new_line}')