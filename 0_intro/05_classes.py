class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def speak(self, msg):
        print msg

    def say_my_name(self):
        self.speak('Hello, my name is ' + self.first_name + ' ' + self.last_name)

# instantiate a new instance of a person.
rusty = Person('Rusty', 'Green')

# notice "self" is never passed when calling the method.
rusty.say_my_name()

# we can access properties on the instance too!
print rusty.first_name
