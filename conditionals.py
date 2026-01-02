# conditionals (if, elif, else) and comparisons

color = input("What is your favorite color? ")
print("\nMy favorite color is", color)

fav_nr = input("\nWhat is your favorite number? ")
fav_nr_int = int(fav_nr)
print("Your number times two is", fav_nr_int * 2)

# x != y (not equal)
# x < y (less than)
# x > y (greater than)
# x == y (equal to)

if fav_nr_int > 100:
    print("\nThat is a big number")
elif fav_nr_int < 10:
    print("\nEasy to guess")
else:
    print("\nVery nice!")

pet = "Ozzy"

if pet == "Ozzy":
    print("\nPurr!")
else:
    print("\nHello little buddy") 
    
pet_type = input("What kind of pet do you have? ")

if pet_type.lower() == "cat":
    print("\nWhoa! I love cats!")
elif pet_type.lower() == "dog":
    print("\nAww dogs are cute!")
else:
    print("\nHmm.. That's an interesting choice")