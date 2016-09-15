class Person:
    # constructor for the class
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def speak(self, msg):
        print msg

    def say_my_name(self):
        self.speak('Hello, my name is ' + self.firstName + ' ' + self.lastName)


# pull functionality of a "person" into a "student"
class Student(Person):
    # constructor
    def __init__(self, firstName, lastName, studentId):
        # note, we are calling the person constructor - so it can do its thing too
        Person.__init__(self, firstName, lastName)
        self.studentId = studentId

    def say_my_id(self):
        self.speak('My student id # is: ' + str(self.studentId))

# we have access to methods and properties from student and person
rusty = Student('Rusty', 'Green', 1234)
rusty.say_my_name()
rusty.say_my_id()
