def logicalOperation():
    has_high_income = True
    has_good_credit = True
    has_criminal_record = False
    
    if has_high_income and has_good_credit:
        print("Eligible for loan")

    if has_good_credit or has_good_credit:
        print("Eligible for loan")

    if has_good_credit and not has_good_credit:
        print("Eligible for loan")

def comparisonOperators():
    name = input("What is your name? ")

    if(len(name) < 3):
        print("name must be at least 3 characters long")
    elif(len(name) > 50):
        print("name can be a maximum of 50 characters")
    else:
        print("name looks good")

def weightConverter():
    weight = input("Weight: ")
    typeOfWeight = input("(L)lbs or (K)g: ")

    if(typeOfWeight == "L" or typeOfWeight == "l"):
        newWeight = float(weight) * 0.45
        msg = f'You are {newWeight} kilos'
        print(msg)
    elif(typeOfWeight == 'k' or typeOfWeight == 'K'):
        newWeight = float(weight) / 0.45
        msg = f'You are {newWeight} lbs'
        print(msg)
    else:
        print("Wrong input")

def whileLoops():
    x = 1
    while(x < 10):
        print('x' * x)
        x += 1

def guessGameUsingWhileLoop():
    secret_numer = 9
    guessCount = 0
    guess_limit = 3
    while(guessCount < guess_limit):
        userInput = int(input("Guess: "))
        guessCount += 1
        if(userInput == 9):
            print("You Won!!")
            break
    else:
        print("You lost!")

def carGame():
    started = False
    userInput = input(">")
    while(userInput != "quit"):
        if(userInput == "help"):
            print('''
start - to start the car
stop - to stop the car
quit - to exit''')
        elif(userInput == "start"):
            if started:
                print("Car is already started")
            else: 
                print("Car started...")
                started = True
        elif(userInput == "stop"):
            if not started:
                print("Car is already stopped!")
            else:
                started = False
                print("Car stopped!")
        else:
            print("I don't understand that...")
        userInput = input(">")

def forLoops():
    # for x in 'python':
    #     print(x)

    # for x in ['Mosh', 'John', 'Sarah']:
    #     print(x)
    
    # for x in range(5, 10, 2): # step 2
    #     print(x)

    y = 0
    for x in [10, 20, 30]:
        y += x
    print(y)

def nestedForLoopToPrintF():
    numbers = [5, 2, 5, 2, 2]

    for x in numbers:
        for y in range(0, x):
            print("F", end="")
        print()

def listsPractice():
    names = ['utkarsh', 'karki', 'shree', 'kalpz']
    print(names[-1]) # returns new list
    print(names[2:])
    print(names[1:3])
    print(names[:3])
    names[0] = "Utkarsh"
    print(names)

def findTheLargestNumberInTheList():
    numbers = [34, 235, 234, 233, 76, 36]
    largest = numbers[0]
    for x in numbers:
        if(x > largest):
            largest = x

    print(largest)

def TwoD_Matrix_Practice():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(matrix[0][2])

    for row in matrix:
        for item in row:
            print(item, end="")
        print()

# logicalOperation()
# comparisonOperators()
# weightConverter()
# whileLoops()
# guessGameUsingWhileLoop()
# carGame()
# forLoops()
# nestedForLoopToPrintF()
# listsPractice()
# findTheLargestNumberInTheList()
TwoD_Matrix_Practice()


