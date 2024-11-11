class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Occupation: {self.occupation}"

# Example Usage
person1 = Person(name="Alice", age=30, occupation="Engineer")
person2 = Person(name="Bob", age=45, occupation="Doctor")

print(person1.display_info())
print(person2.display_info())
