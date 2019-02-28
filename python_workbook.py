# Exercise 34

integer = int(input("Enter an integer: "))
if integer % 2:  
  print(f"The integer is odd")
else:  
  print(f"The integer is even")

# Exercise 35

human_age = int(input("Enter the human_age: "))

if human_age == 1 or human_age == 2:
  dog_age = human_age * 10.5
  print(human_age * 10.5)
  print(f"the dog_age is {dog_age}")
else: 
  dog_age = (human_age - 2) * 4 + 21 
  print(dog_age)
  
  # Exercise 36 
  
  letter = input("Enter a letter of the alphabet: ") 
vowel = ['a', 'e', 'i', 'o', 'u']
if letter == 'a' or letter == 'e' or letter == 'i' or letter =='o' or letter == 'u':
  print("The letter is a vowel")
elif letter == "y": 
  print("Sometimes y is a vowel sometimes a constonant")
else: 
  print("The letter is a constonant")
  
  # Exercise 37
  
  sides = int(input("Enter the number of sides in a shape: "))
if sides == 3:
  print(f"The shape is a triangle")
elif sides == 4:
  print(f"The shape is a quadrilateral")
elif sides == 5:
  print(f"The shape is a pentagon")
elif sides == 6:
  print(f"The shape is a hexagon")
elif sides == 7:
  print(f"The shape is a heptagon")
elif sides == 8:
  print(f"The shape is a octagon")
elif sides == 9: 
  print(f"The shape is a nonagon")
elif sides == 10:
  print(f"The shape is a decagon")
else: 
  print("error")
  
  # Exercise 48
  
  year = int(input("Enter any year: "))
if year % 12 == 8: 
  print(f"the animal is a dragon")
elif year % 12 == 9: 
  print(f"the animal is a snake")
elif year % 12 == 10: 
  print(f"the animal is a horse")
elif year % 12 == 11:
  print(f"the animal is a sheep")
elif year % 12 == 0:
  print(f"the animal is a monkey")
elif year % 12 == 1:
  print(f"the animal is a rooster")
elif year % 12 == 2:
  print(f"the animal is a dog")
elif year % 12 == 3:
  print(f"the animal is a pig")
elif year % 12 == 4:
  print(f"the animal is a rat")
elif year % 12 == 5:
  print(f"the animal is a ox")
elif year % 12 == 6:
  print(f"the animal is a tiger")
elif year % 12 == 7:
  print(f"the animal is a hare")
  
  
