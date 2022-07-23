print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower()!= "yes":
    quit()

print("Okay! Let's play :) ")
score = 0;
answer = input("What does CPU stand for ?")

if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for ?")

if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

    answer = input("What does RAM stand for ?")

if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

    answer = input("What does PSU stand for ?")

if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
    
a = 4
    # print("you got " + str(score)+ "questions correct")
txt="You got {0} out of {1} points in the quiz."
print(txt.format(score,a))