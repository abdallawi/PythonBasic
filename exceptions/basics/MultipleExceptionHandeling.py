try:
    age = int(input('Please fill in your age: \n'))
    x_factor = 42 / age
    print(x_factor)
except (ValueError , ZeroDivisionError, KeyboardInterrupt) as ze:
    print('Something went wrong all in the dark ')
    print(ze)
except OSError as ose:
    print(ose.with_traceback())
    print('OS error')

