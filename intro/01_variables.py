# This program says hello and asks for my name.
print('Hello world!')
print('What is your name?')  # ask for their name
myName = raw_input()

print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?')  # ask for their age
myAge = input()

# concatenate age
print('Hello ' + myName + ' you will be ' + str(myAge + 1) + ' in a year.')
