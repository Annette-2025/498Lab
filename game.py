import random

def ask_question(question, answer):
    user_answer = input(question + " ")
    return user_answer.lower() == answer.lower()    #return result of comparison (put all in lowercase to prevent silly issues with capitalization)

def main():
    questions = {
        "What is the capital of France?": "paris",
        "What is 2 + 2?": "4",
        "What is the color of the sky?": "blue",
        "Who wrote 'To Kill a Mockingbird'?": "harper lee",
        "What is the largest planet in our solar system?": "jupiter"
    }

    score = 0
    question_list = list(questions.keys())
    random.shuffle(question_list)

    for question in question_list:  #while list has next and assign next question to "question"
        if ask_question(question, questions[question]): #if function returns true
            print("Correct!")
            score += 1
        else:
            print("Wrong!")

    print(f"Your final score is {score} out of {len(questions)}")
    # just some friendly feedback at the end of the quiz:
    if score == 0:
        print("you failed, there is no hope for you!")
    else:
        if score < 3:
            print("that sucked, you didn't even get half!")
        else:
            if score < 5:
                print("actually try next time!")
            else:
                print("congrats, you actually passed.")


# for some reason, this is the only way the main function can be entered
if __name__ == "__main__":
    main()