# Classes practice?
'''
Project description:
Building a test with question/answer pairs
built into a class
'''
class Questionz:
    def __init__(self,questionarg,answerarg):    
        self.question = questionarg
        self.answer = answerarg

list_of_questions = [
    "What is 5 + 10?",
    "When did Estonia become independent?",
    "What is 7 * 7?"
]
answerz = [
    Questionz(list_of_questions[0],15),
    Questionz(list_of_questions[1],1918),
    Questionz(list_of_questions[2],49)
]
def test():
    global score
    score = 0
    for q in answerz:
        print(q.question)
        prompt = int(input())
        if prompt == q.answer:
            score += 1
    print(f"Your score is {score}/{len(list_of_questions)}!")
def add_questions():
    global adding
    while adding:

        qadd = input("Please enter the question you would like to add here:\n")
        list_of_questions.append(qadd)
        compprompt = input("Thank you for your question! would you like to add another? True/False ").upper()
        if compprompt == 'False':
            adding = False
        print("Alright! Thank you!")

which_one = input("would you like to answer a question or add one? (1/2) ")
if which_one == '1':
    test()
else:
    add_questions()
        
