#This program will calculate the equivalent grade of the score with base 50 with remarks.
#   by BSMATH 1-3: Ceriola, Princess Mae; Galves, Leomar; Malipico, Jennyflor Grace, and Ramos, Clydes


def EG():
    print("Welcome to Grade Equivalent Calculator! \nThis program allows you to calculate your equivalent grade according to the score in base 50")
    S=eval(input("Enter the score of your exam: "))
    PS=eval(input("Enter the perfect score of the exam: "))
    E=((S/PS)*50)+50
    print("Your equivalent grade is",round(E,2),".")
    if(E>95 and E<=100):
        print("Excellent! You did great!")
    elif(E>90 and E<=95):
        print("Very Good! Keep it up!")
    elif(E>85 and E<=90):
        print("Good! You're really improving")
    elif(E>80 and E<=85):
        print("Keep working on it! You can do better!")
    elif(E>75 and E<=80):
        print("Work harder! You can do it!")

    else:    
        print("You failed! You need extra effort & study harder!")


EG()
