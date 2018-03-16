questions = (input("What is your name? "),
             input("What is your favorite color? "),
             input("What is your quest? "),)

i = 0
while True:
    answers = (questions[i])
    i = (i+1) % 3


