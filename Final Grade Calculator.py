#This program will compute the student's final equivalent grade in Mathematical Computing 1
#   By: Leomar Tagle
#       BSMATH 1-3

print("Welcome to Mathematical Computing 1 Final Grade Calculator!")
print( )
print("This program allows you to compute your final grade in Mathematical Computing 1")
print(" by entering your scores in long exam, programming exercise, python interaction, and final exam")
print( )
firstname=input("Enter your first name: ")
lastname=input("Enter your last name: ")
print( )
print("Hi",firstname.title()+"!"" ""Your final grade composed of 70% of the class standing and 30% of the major exam")
print("The class standing grade are divided into 3 category: ") 
cs1="               50% of Long Exam"
cs2="               35% of Programming Exercise"
cs3="               15% of Python Interaction"
print(cs1)
print(cs2)
print(cs3)
print("Your grade per category is calculated as the average of your equivalent grade (base 50) of each score")
print("The final grade that I will post is based on the PUP Grading System")
print( )

print("Kindly prepare your scores and the perfect scores of the following: ")
a1="                Long Exam"
a2="                Programming Exam"
a3="                Phyton Interaction"
print(a1)
print(a2)
print(a3)
print( )
print( )

def first(activity):
    
    n=int(input("How many "+activity+" did you have? "))
    print( )
    EQG=0
    
    for i in range(n):
            score=float(input("Enter your score in "+activity+" "+ str(i+1) +": "))
            perfectscore=float(input("Enter the perfect score in "+activity+" "+ str(i+1) +": "))
            EQ=(((score/perfectscore)*50)+50)
            EQG+=EQ

    pg=EQG/n

    print("The final grade of your "+activity+" is",str(pg)+".")
    

def activity():
    
    first("Long Exam")
    LEG=float(input("Enter your long exam grade: "))
    print( )
          
    first("Programming Exercise")
    PEG=float(input("Enter your programming exercise grade: "))
    print( )
    
    first("Python Interaction")
    PIG=float(input("Enter your python interaction grade: "))
    print( )
    
    first("Major Exam")
    MEG=float(input("Enter your major exam grade: "))
    print( )
    
    fgrade=((((LEG*0.5)+(PEG*0.35)+(PIG*0.15))*0.7)+(MEG*0.3))
    print("Your Final Grade in Mathematical Computing 1 is",str(round(fgrade,2))+".")
    print( )
    print( )
    
    print("Hello",firstname.title()+"!"" ")
    print("Your Final Grade in Mathematical Computing 1 is",str(round(fgrade,2))+".")
    if(fgrade>97 and fgrade<=100):
        print("Your equivalent grade based on PUP Grading System is",str(1.0)+".")
        print("Superb! I commend you for your thorough work!")
    elif(fgrade>94 and fgrade<=96):
        print("Your equivalent grade based on PUP Grading System is",str(1.25)+".")
        print("Terrific! I commend you for your thorough work!")
    elif(fgrade>91 and fgrade<=93.99):
        print("Your equivalent grade based on PUP Grading System is",str(1.5)+".")
        print("Nice! You such a great student!")
    elif(fgrade>88 and fgrade<=90.99):
        print("Your equivalent grade based on PUP Grading System is",str(1.75)+".")
        print("Nice! You such a great student!")
    elif(fgrade>85 and fgrade<=87.99):
        print("Your equivalent grade based on PUP Grading System is",str(2.0)+".")
        print("Wow! you are doing great!")
    elif(fgrade>82 and fgrade<=84.99):
        print("Your equivalent grade based on PUP Grading System is",str(2.25)+".")
        print("Fabulous! You such great student!")
    elif(fgrade>79 and fgrade<=81.99):
        print("Your equivalent grade based on PUP Grading System  is",str(2.5)+".")
        print("Fabulous! You such great student!")
    elif(fgrade>76 and fgrade<=78.99):
        print("Your equivalent grade based on PUP Grading System is",str(2.75)+".")
        print("You are doing great! Continue studying! ")
    elif(fgrade>75 and fgrade<=75.99):
        print("Your equivalent grade based on PUP Grading System is",str(3.0)+".")
        print("Good grade! Continue studying, I knew you could do it!")
    else:
        print("Your equivalent grade based on PUP Grading System is",str(5.0)+".")
        print("Sorry, you failed! Exert more effort in studying!")
    print( )
    print("Thank you for using our Grade Calculator! Have a Good Day Mr/Ms",lastname.title()+"!"" ")
           
activity()
