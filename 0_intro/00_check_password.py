secretPassword = open('assets/secret_password_file.txt').read()
typedPassword = raw_input("What's the secret password?")

if typedPassword == secretPassword:
    print('Access granted')
else:
    print('Access denied')