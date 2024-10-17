def new_game():
    guesses=[]
    correct_guesses=0
    question_num=1

    for key in questions:
        print("----------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess=input("Enter (A, B, C OR D): ")
        guess=guess.upper()
        guesses.append(guess)
        correct_guesses += check_ans(questions.get(key),guess)

        question_num+=1
    display_score(correct_guesses,guesses)
def check_ans(answer,guess):
    if answer==guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0


def display_score(correct_guesses,guesses):
    print("-------------------")
    print("RESULTS")
    print("--------------------")
    print("GUESSES: ",end=" ")
    for i in guesses:
        print(i,end=" ")
    print()
    score=int((correct_guesses/len(questions))*100)
    print("Your Score is: "+str(score)+"%")


def play_again():
    pass


questions={ "Who created Python: ":"A","What year was python created: ":"B","Python is tributed to which comedy group? ":"C","Is the earth round? ":"A" }

options=[["A. Guido van Rossum","B. Elon musk","C. Bill Gates","D. Mark Zuckerburg"],["A.1989","B.1991","C.1994","D.2004"],["A.Lonely island","B.Smosh","C.Monty python","D.snail"],["A.true","B.false","C.sometimes","D.whats earth"]]

def play_again():

    response=input("Do you want to play again?(Yes/No):  ")
    response=response.upper()

    if response=="YES":
        return True
    else:
        return False

new_game()

while play_again():
    new_game()

print("BYE")
