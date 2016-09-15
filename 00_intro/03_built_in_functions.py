# https://docs.python.org/2/library/functions.html

my_true = True
my_false = False
my_int = 4
my_float = 1.0

print 'I can concatenate types, but I have to convert them to a string. See: ' + \
      str(my_true) + ' ' + \
      str(my_int) + ' ' + \
      str(my_float)

test = bool('True')
test = str(12345)
test = int('123')
test = float('2.434')

print (type(123))
your_name = raw_input('Hey, what\s your name?')

print (min(32, 36, 47, 2345, 3456, 34, 2, 3456))
print (max(32, 36, 47, 2345, 3456, 34, 2, 3456))

# TODO: Add example of all, any, filter, etc...
