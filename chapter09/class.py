class Pet():
    def __init__(self, name, age):
        self.name = name
        self.age = age
# my_pet = Pet('willie', 6)
# print("My pet's name is " + my_pet.name.title() + ', his is ' + str(my_pet.age) + ' years old.')

# 继承
class PetKind(Pet):
    def __init__(self, name, age, kind):
        super().__init__(name, age)
        self.kind = kind
my_petKind = PetKind('willie', 6, 'dog')

print('My ' + my_petKind.kind + "'s name is " + my_petKind.name + ', his is ' + str(my_petKind.age) + ' years old.')
