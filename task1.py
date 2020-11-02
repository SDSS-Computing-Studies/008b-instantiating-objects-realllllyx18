#!python3

"""
Create a class that will store a database for a veterinarian.
Your class will need the following properties:

animal (dog, cat, fish, bird, turtle, etc)
breed
name (the pet's name)
owner (the owner's name)
birthdate (of the pet, expressed as yyyy-mm-dd)

The constructor will need to ask for each of those values
for the database when the pet is instantiated

Methods:
display() - should show the name of the pet and type followed by their breed and owner


Main block should have a menu that has the following options:
1. Enter a new pet
2. Retrieve a pet
3. Exit

If they choose to retrieve a pet,
display the following:
Enter pet's name:
and then go through the list, looking for the name of the pet.
If the pet is found, it should call the display() method from the object

Example output:
1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? cat
Breed? Domestic Long Hair
Name? Benjamin
Owner? Chris
Birthdate? 20015-10-01

1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? dog
Breed? Shih-tzu
Name? Buster
Owner? Christy
Birthdate? 2008-10-16

1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? cat
Breed? Domestic Long Hair
Name? Casey
Owner? Chris
Birthdate? 20015-10-01

1. Enter a new pet
2. Retrieve a pet
3. Exit
2

Which Pet? Buster

Buster dog
Shih-tzu is owned by Christy
(10 points) 
"""

class animal:
    animaltype = None
    breed = None
    name = None
    owner = None
    birthdate = None
    num = None

    def __init__(self):
        self.animaltype = input("Type of animal?")
        self.breed = input("Breed?")
        self.name = input("Name?")
        self.owner = input("Owner?")
        self.birthdate = input("Birthdate?")

    def display(self):
        length = len(self.name)
        print(self.name)
        print(self.animaltype)
        print(self.breed)
        print("is owned by:" + self.owner)

def main():
    animals = []
    num = 0
    while 1 > 0:
        print("1. Enter a new pet\n" + "2. Retrieve a pet\n" + "3. Exit")
        num = int(input("Choose number 1, 2, or 3:"))
        if num == 1:
            animals.append(animal())
        if num == 2:
            length = len(animals)
            inputname = input("Enter the name of the pet:")
            for i in range(0,length):
                petname = animals[i].name
                if petname == inputname:
                    animals[i].display()
        if num == 3:
            print("Goodbye.")
            break

main()

            


            

