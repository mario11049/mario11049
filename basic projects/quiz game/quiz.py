print("welcome to the quiz!")
print("your score will be calculated based on your annswers")
print("ypur score is 0")
score = 0
answer1 = input("whats the capital of delhi?")
if answer1 == "delhi":
    print("corect answer")
    score +=1
else:
    print("wrong answer")
answer2 = input("whats 5 + 5")
if answer2 == "10":
    print("correct answer")
    score +=1
else:
    print("wrong answer")
answer3 = input("what is my name?")
if answer3 == "manoj":
    print("correct answer")
    score +=1
else:
    print("wrong answer")
print("your final score is ", score)