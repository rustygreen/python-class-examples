# print ('hello, what\'s your name')
# print ('C:\Workspace\my_folders\my_file.txt')

# my_content = open('my_file.txt')  # same folder
# my_content = open('../assets/my_file.txt')  # relative path
# my_content = open(r'C:\Workspace\my_folders\my_file.txt')  # absolute path

# One way to do it
my_age = 234
my_file = open(r'..\assets\text.txt', 'w')
my_file.write('rusty' + my_age)
my_file.close()

# Here is another:
with open(r'..\assets\text.txt', 'w') as my_file:
    my_file.write('rusty')

