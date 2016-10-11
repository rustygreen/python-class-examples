"""
1) Create a list with 3 peoples names in it (set it to a variable)
2) Next line, add a new name to the list
3) Loop through the list, and print each name
"""

names = [{'name': 'john', 'age': 31}, {'name': 'bob', 'age': 24}, {'name': 'jane', 'age': 42}]

# Add a new item, with the "append" method.
names.append({'name': 'rusty', 'age': 31})

for person in names:
    # name variable only exists in this block
    print(person['name'])
    print(person['age'])
