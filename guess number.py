import random

computer_number = random.randint(10 , 40)
attempts = 0

for i in range(10):
    user_number = int(input("guess the number between 10 and 40"))
    attempts += 1

if computer_number == user_number:
    print("congratulations! you win")
    print(f"number of attempts:{attempts}")
    

elif computer_number > user_number:
    print("guess a larger number")
elif computer_number < user_number:
    print("guess a smaller number")
    