secret_password = open('../assets/secret_password_file.txt').read()
user_password = raw_input("What's the secret password?")

if user_password == secret_password:
    print('Access granted')
else:
    print('Access denied')
