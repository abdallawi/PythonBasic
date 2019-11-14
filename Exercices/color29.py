color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
delta_color = []
for color in color_list_1:
    if color not in color_list_2:
        delta_color.append(color)
print(delta_color)
