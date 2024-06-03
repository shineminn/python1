random_gauss1 = input ("Enter Head or Tail: ")
import random
coin_toss = ["Head", "Tail"]
random_gauss2 = random.choice(coin_toss)
print (random_gauss2)

if random_gauss1 == "Head" and random_gauss2 == "Head":
    print ("You won")
elif random_gauss1 == "Head" and random_gauss2 == "Tail":
    print ("You lose")
elif random_gauss1 == "Tail" and random_gauss2 == "Tail":
    print ("You won")
elif random_gauss1 == "Tail" and random_gauss2 == "Head":
    print ("You lose")
else:
    print ("system Error")