# 130
class Pets():
    animals = []

    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())


class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'


class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'


class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'


# 1 Add another Cat
class George(Cat):
    def sing(self, sounds):
        return f"{sounds}"


# 2 Create a list of all of the pets (create 3 cat instances from the above)
my_cats = [Simon("Simon", 1), Sally("Sally", 2), George("George", 3)]

# 3 Instantiate the Pet class with all your cats use variable my_pets
my_pets = Pets(my_cats)
# 4 Output all of the cats walking using the my_pets instance
my_pets.walk()


# 146
def multiply_by_2(item):
    return item * 2


print(list(map(multiply_by_2, [2, 4, 6])))

myList = [2, 4, 6]
newList = list(map(lambda num: num ** 2, myList))
print(newList)

listSort = [(0, 2), (4, 3), (9, 9), (10, -1)]
listSort.sort(key=lambda x: x[1])
print(listSort)
