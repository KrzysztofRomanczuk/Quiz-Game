def new_game():

    guesses = []
    correct_guesses = 0
    questions_num = 1

    for key in questions:
        print("-------------------------------")
        print(key)
        for i in options[questions_num-1]:
            print(i)

        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key),guess)
        questions_num += 1

    display_score(correct_guesses,guesses)

#------------------

def check_answer(answer, guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong!")
        return 0

#------------------

def display_score(correct_guesses, guesses):
    print("-------------")
    print("RESULTS")
    print("-------------")

    print("Answer: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")


#------------------

def play_again():
    response = input("Do you want play again? (Yes or No):")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
#------------------


questions = {"Who created Python?:": "A",
             "What year was Python created?:": "B",
             "What is a correct syntax to output 'Hello World' in Python?:": "B",
             "Which Python framework is mostly used?:": "D",
             "The most useful languages in machine learning is?:": "C",
             }
options = [
    ["A. Guido van Rossum","B. Bill Gates","C. Mark Zuckerberg","D. Jeff Bezos"],
    ["A. 1989","B. 1991","C. 2001","D. 2011"],
    ["A. echo(Hello World)","B. print(Hello World)","C. p(Hell World)","D. paste(Hell World)"],
    ["A. Flask","B. React", "C. Node.JS", "D. Django"],
    ["A. Cobol, Fortan, Basic", "B. Swift, Kotlin, Dart", "C. Python, R, Java", "D. SQL, HTML, PHP"]
]

new_game()

while play_again():
    new_game()

print("See you next time!")








