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

class animals:
    Pet = None
    Retrieve = None
    Breed = None
    Name = None
    Owner = None
    Birthdate = None
    
    def __init__(self):
        self.Pet = input("Type of animal?")
        self.Breed = input("Breed?")
        self.Name = input("Name?")
        self.Owner = input("Owner?")
        self.Birthdate = int(input("Birthdate?"))

    def displayPet(self):
        self.Retieve = input("Which pet?")
        output1 = str(self.Name + " " + self.Pet)
        output2 = str(self.Breed + " is owned by " + self.Owner)
        print(output1)
        print(output2)
    
    def  __del__(self):
        print("Goodbye.")

    #def index(self):
        #index = input("Enter the index: ")
        #if index == "1":
        #    __init__(self)
        #if index == "2":
        #    displayPet(self)
        #if index == "3":
            #return

def main():
    animal = []
    num = 0
    while 1 > 0:
        input("1. Enter a new pet\n" + "2. Retrieve a pet\n" + "3. Exit\n")
        if num == 1:
            for i in range(0,3):
                animal.append(animals())
        if num == 2:
            print(output1)
            print(output2)
        if num == 3:
            print("Goodbye.")
            break
main()

            


            

