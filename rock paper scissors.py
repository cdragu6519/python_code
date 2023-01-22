import random

choices = ["r", "p", "s"]
print("Lets play some rock paper scissors")

user = "r"  # temporary value
isValid = False
while not isValid:
    user = input("make your choice = ")
    if user in choices:
        isValid = True
        print('user chose:', user)
    else:
        print("wrong letter, only r, p, s allowed")


computer = random.choice(choices)
print('computer chose:', computer)

if user == computer:
    print("its a tie")
else:
    lineup = {
        ('r', 'p'): "computer wins",
        ('r', 's'): "user wins",
        ('p', 'r'): "user wins",
        ('p', 's'): "computer wins",
        ('s', 'r'): "computer wins",
        ('s', 'p'): "user wins",
    }
    print(lineup[(user, computer)])
