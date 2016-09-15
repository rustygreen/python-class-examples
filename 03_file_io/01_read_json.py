import json

with open(r'assets\people.csv', 'w') as f:
    f.write('one, two, three')
    with open(r'assets\people.json') as data_file:
        people = json.load(data_file)
        for person in people:
            f.write(person['firstName'] + '\n')
            print person['firstName']
