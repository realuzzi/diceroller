import random

print("My Dice Roller")
print("-----------------")

print("How many dice would you like to roll?")
### Validate Input
while True:
  try:
    numberPicked = int(input("Type an integer between 1 and 20: "))
    if(numberPicked > 0 and numberPicked < 20):
      break
    else:
      print("Invalid input. Try Again.")
  except:
    print ("Please provide an integer")

def rollDice(amountofDice):
  totalSum = 0
  possibleFaces = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
  for die in range(amountofDice):
    roll = random.choice(possibleFaces)
    print("Die", die + 1, ":", roll)
    totalSum += roll 
  print("Total sum: ", totalSum)
  

rollDice(numberPicked)