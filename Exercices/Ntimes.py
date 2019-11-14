num = int(input('Enter a number:\n'))
a = int('%s' % num)
b = int('%s%s' % (num, num))
c = int('%s%s%s' % (num, num, num))

print( a + b + c)

