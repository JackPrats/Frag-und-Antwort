import csv

questions = [input("What is your name?"),
             input("What is your favorite color?"),
             input("What do you seek?")]

n = 0
while True:
    print("Type q to quit")
    answer = input(questions[n])
    if answer == "q":
        break
    n = (n + 1) % 3

with open(answers.csv, "w+") as f:
    r = csv.writer(f)

