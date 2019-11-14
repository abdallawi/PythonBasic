Sample_String = "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high," \
                " Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
first_str = "Twinkle, twinkle, little star,\n"
second_str = "How I wonder what you are!\n"
third_str = "Up above the world so high,\n"
fourth_str = "Like a diamond in the sky.\n"

print(f'{first_str}\t{second_str}\t\t{third_str}\t\t{fourth_str}'
      f'{first_str}\t{second_str[:len(second_str)-2]}')

