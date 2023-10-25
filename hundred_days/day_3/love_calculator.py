print("Welcome to your love calculator")

first_name = input("Enter your name: ")
second_name = input("Enter partner's name: ")

full_name = first_name + second_name
full_name_lower = full_name.lower()

t = full_name_lower.count("t")
r = full_name_lower.count("r")
u = full_name_lower.count("u")
e = full_name_lower.count("e")

true = t+r+u+e

l = full_name_lower.count("l")
o = full_name_lower.count("o")
v = full_name_lower.count("v")
e = full_name_lower.count("e")

love = l+o+v+e

love_score = int(str(true)+str(love))

if love_score < 10 or love_score > 90:
    print(f"Your lover score is {love_score}, you are like coke and menthos")

else:
    print("you match")
