# Modify this function to return a list of strings as defined above
def list_benefits():
    return [ "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    t = benefit + " -"
    return t

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

#name_the_benefits_of_functions()

# define the Vehicle class
class Vehicle:
    def __init__(self,name, kind, color, value):
        self.name = name
        self.kind = kind
        self.color = color
        self.value = value
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here
car1 = Vehicle("Fer","car","red",60000.00)
car2 = Vehicle("Jump","van","blue",10000.00)
# test code
print(car1.description())
print(car2.description())

phonebook = {"John" : {938477566,"A"},"Jack" : {938377264,"B"} }
for name, number in phonebook.items():
    print("Phone number of %s is %d in %s" % (name, number())
    
   