"""
"The yield statement" section example of psychologist session

"""


def psychologist():
    print('Please tell me your problems')
    while True:
        answer = (yield)

        if answer is not None:
            if answer.endswith('?'):
                print("Don't ask yourself too much questions")
            elif 'good' in answer:
                print("Ahh that's good, go on")
            elif 'bad' in answer:
                print("Don't be so negative")
            elif answer in ('q', 'quit'):
                print("Goodbye")
                yield
                return
            else:
                print("Please continue")


if __name__ == "__main__":
    print("Starting psychologist session, type 'q' or 'quit' to end session")

    freud = psychologist()

    for phrase in freud:
        problem = input("> ")
        freud.send(problem)
