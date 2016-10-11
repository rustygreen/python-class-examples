import json
import datetime
import uuid
from dateutil.parser import parse

with open(r'..\assets\people.csv', 'w') as f:
    f.write('First Name, Last Name, Age, Student ID\n')
    with open(r'..\assets\people.json') as data_file:
        people = json.load(data_file)
        student_id = 1
        for person in people:
            birth = parse(person['birthday'])
            age = (datetime.datetime.now() - birth).days
            age = age / 365
            csv_row = person['firstName'] + ', ' + person['lastName'] + ', ' + str(age) + ', ' + str(
                uuid.uuid4()) + '\n'
            print (csv_row)
            f.write(csv_row)
            student_id += 1
