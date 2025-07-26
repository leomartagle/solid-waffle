#This program will compute the amount to be charged by a taxi
#By Leomar Tagle of BS Mathematics 1-3

def charge():
    print("This program will compute the amount to be charged by a taxi") #opening statement
    print("   P40.00 will be automatically charged for the flag down rate.") #flag down rate
    print("   P13.50 will be charged per kilometer.") #rate per kilometer
    print("   P2.00 will be charged per minute.") #rate per minute
    d=float(input("Enter the distance you've travelled in kilometers(km):")) #input, assignment statement 1
    t=float(input("Enter the number of minutes it was travelled:")) #input, assignment statement 2
    c=40.00+(13.50*d)+(2.00*t) #process
    print("The amount to be charged by a taxi should be P",c) #output statement

charge()
            

