from random import randint
import time


def create_mathformula(n):   # to create the final expression that will be evaluated
    operations = ['+', '-', '*', '/']  # possible operators
    mathformula = ""
    for k in range(n):
        if k != n-1:
            number1 = randint(0, 100)  # defining a random number between 1 and 100
            op = operations[randint(0, 3)]  # defining a random operation between the ones in the array
            mathformula += f"{number1} {op} "  # obtaining a new part of the expression
        else:
            number = randint(0, 100)
            mathformula += f"{number} "
    return mathformula


def evaluate_mathformula(mathformula):
    try:
        return eval(mathformula)  # evaluating the expression as a mathematical formula
    except Exception as error:
        print(f"ERROR! The encountered error is: {error}. Generate again random exercises.")
        exit()


def main():
    print("Our student ID are 2256329 - 2256322")
    userinput = True
    while userinput:  # to continue infinitely if the user types "Proceed"
        n = 10  # number of operations per cycle
        print("\nThe number of operations to be performed is", n)
        wrongexercises = []
        start_time = time.time() # in order to start the timer
        for j in range(n):
            nmboperators = randint(3, 5)  # define the number of operators in a line
            line = create_mathformula(nmboperators)
            result = round(evaluate_mathformula(line), 2)  # define the result using the function "evaluate_mathformula()"
            print(line)
            ok = False  # to check if the input is correct or not
            while not ok:
                try:
                    resultuser = round(float(input("Please enter your answer: ")), 2)
                    ok = True
                except Exception as error:
                    print(error)  # to deal with errors
            print("Thanks!")
            if resultuser != result:
                totalline = f"{line} = {result}"
                wrongexercises.append(totalline)  # add the wrong exercises to the list of wrong ones
        print(f"Total time: {round(time.time() - start_time, 2)} seconds") # to find out which is the time
        print(f"The number of correct answers is {n - len(wrongexercises)}")  # since there are n exercises and all the wrong ones are inserte in the list
        print("The following are the right answers of the questions you got wrong:")
        for i in range(len(wrongexercises)):
            print(wrongexercises[i])
        listpossible = ["proceed", "exit", "1", "2"]
        ok = True  # to check if the input is possible or not (in order to proceed or exit)
        print("Whether to proceed to the next round of testing? Please input:\n1. Proceed\n2. Exit")
        while ok:
            contuser = input("Your input: ")  # input to show if you want to continue or not
            if contuser.lower() in listpossible:
                ok = False
            else:
                print("Not possible input. Try again :(")
        if contuser.lower() == "exit" or contuser.lower() == "2":
            userinput = False


if __name__ == '__main__':
    main()
