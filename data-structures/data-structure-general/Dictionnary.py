
new_line = '\n'
first_key = 'x'
second_key = 'y'
third_key = 'z'
invalid_key = 'invalid key'

msg_x = 'the value of x is: '
msg_y= 'the value of y is: '
msg_z = 'the value of z is: '
mem_loc_msg = 'memory location: '

first_point = {first_key: 1, second_key: 2}

sec_point = dict(x=1, y=2)
print(f'{first_point} {mem_loc_msg} {id(first_point)}')
print()
print(f'{sec_point} {mem_loc_msg} {id(sec_point)}')
first_point[first_key] = 5
first_point[third_key] = 14

print(f'{msg_z} {first_point["z"]}', new_line)

if invalid_key in first_point:
    print('Never gonna happen, so no error for you! Good job :D')

del first_point['z']
print(first_point)

for key in first_point:
    print(f'key: {key} value {first_point.get(key)}')

for t in first_point.items():
    print(t)
else:
    print()

for key, value in first_point.items():
    print(F"{'The key:'} {key} {'holds the value:'} {value}")

x = first_point.get('x', )
print(x)