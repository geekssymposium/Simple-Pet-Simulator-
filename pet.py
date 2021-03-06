#First created a Dog and Cat class
#Took all the common methods from the 2 and created another class called Animals
#inherited those common methods from Animals to Dog and Cat class


class Animals:
    def __int__(self,name):
        self.name = name
    def walk(self):
        print(f"{self.name} is walking ")
    def feed(self):
        print(f"{self.name} is eating ")
    def wash(self):
        print(f"{self.name} is taking a shower ")
    def __del__(self):
        pass



class Dog(Animals):
    def __init__(self,name):
        self.name = name
    def bark(self):
        print(f"{self.name} is barking ")
    def help(self):
        print(f""""
walk - take your dog for a walk
bark - make your dog bark
feed - feed your dog
wash - wash your dog 
name - rename your cat
""")

#############################################################################
class Cat(Animals):
    def __init__(self,name):
        self.name = name
    def annoy(self):
        print(f"{self.name} is annoying you for no good reason")
    def help(self):
            print(f"""
walk - take your cat for a walk
annoy - make your cat annoy you for no good reason
feed - feed your cat
wash - wash your cat 
name - rename your cat
    """)

##############################################################################

#The below booleans(cat and dog) are required for later "rename your pet" function
#Initialized quit to False with the other booleans, required later to quit the program

dog, cat,quit = False,False,False


pet = "none"

while pet == "none":
    choice = input("Choose your pet ! ").lower()
    if choice == 'dog':
        dog = True
        pet = Dog(input("Enter your dog's name ! "))
    elif choice == 'cat':
        cat = True
        pet = Cat(input("Enter your cat's name ! "))
    else:
        pet = "none"
        print("Choose either a cat or dog ")

#############################################################################


while quit == False :

    choice = input("What would you like to do ? ")

    if choice == "walk":
        pet.walk()

    elif choice == "bark":
        try:
            pet.bark()
        except AttributeError:
            print("Your pet can't bark, Dummy !")

    elif choice == "annoy":
        try:
            pet.annoy()
        except AttributeError:
            print("There's no way your pet can annoy you, Dummy !")

    elif choice == "feed":
        pet.feed()

    elif choice == "wash":
        pet.wash()

    elif choice == "help":
        pet.help()

    elif choice == "name":
        if dog == True:
            del pet
            pet = Dog(input("Rename your dog "))
        else:
            del pet
            pet = Cat(input("Rename your cat "))

    elif choice == "quit":
        quit = True

    else:
        print("I don't understand")

