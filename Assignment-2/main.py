class Person:
    # abstract method
    def get_gender(self):
        pass

# child classes
class Male(Person):
    def get_gender(self):
        return "Male"

class Female(Person):
    def get_gender(self):
        return "Female"

male = Male()
female = Female()

print(male.get_gender())  
print(female.get_gender())
