"""class Sample:

    def info(self, name='Guest', salary=45000, place='Pune'):
        self.name=name
        self.Salary=salary
        self.Place=place

    def display(self):
        print("This is a display method.")
        print(f'Name: {name}, Salary: {salary}, Place: {place}')
        print()


# Creating an object of the class
s = Sample()

# Calling the method with arguments
s.info(salary=5000, name='John', place='New York')
s.display()"""
"""
""'class Sample:

    def info(self,name='Guest',salary=45000,place='Pune'):
        # to allow the local members of info to be accessed in other methods
        # we need to make them instance variable using self
        self.name = name # name is local var. and self.name is instance variable
        self.salary = salary
        self.place = place

    def display(self):
        print("This is a display method.")
        print(f'Name: {self.name},\nSalary: {self.salary}, \nPlace: {self.place}')
        print()

# Creating an object of the class
s = Sample()
# Calling the method with arguments
s.info(salary=5000,name="John", place="New York")
s.display()
print(s.__dict__)"""


class Sample:
    def __init__(self):
        print("This IS The Constructor of class Sample")

s1=Sample()
s1=Sample()
s1=Sample()

