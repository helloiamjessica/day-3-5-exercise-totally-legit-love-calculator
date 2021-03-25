# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


name1 = name1.lower()
name2 = name2.lower()

#adding up "True"
name1_trues=name1.count("t") + name1.count("r") + name1.count("u") + name1.count("e")
name2_trues=name2.count("t") + name2.count("r") + name2.count("u") + name2.count("e")

name1_loves=name1.count("l") + name1.count("o") + name1.count("v") + name1.count("e")
name2_loves=name2.count("l") + name2.count("o") + name2.count("v") + name2.count("e")

true_total=name1_trues + name2_trues
love_total=name2_loves + name1_loves


true_love_str = str(true_total) + str(love_total)

true_love_int = int(true_love_str)

#print(true_love_str)

if true_love_int <= 10 or true_love_int >= 90:
  print(f"Your score is {true_love_int}, you go together like coke and mentos.")
elif true_love_int >=40 and true_love_int <=50:
  print(f"Your score is {true_love_int}, you are alright together.")
else:
  print(f"Your score is {true_love_int}.")


