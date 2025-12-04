
def question(q, right_answer):
    print(q)
    a = input()
    if a ==right_answer:
        print("Correct!")
    else:
        print("Incorrect...")


question("What is the capital of China?", "Beijing")
question("What is the capital of Thailand?", "Bangkok")
question("What is the capital of Vietnam?", "Ho Chi Min City")
