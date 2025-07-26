Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #By Leomar Tagle of BS Math 1-3
>>> #Exercises Set A
>>> s1="Happy"
>>> s2="new"
>>> s3="Year!"
>>> #1
>>> s1+"ka?"
'Happyka?'
>>> #2
>>> s1*len(s2)+s2+s3
'HappyHappyHappynewYear!'
>>> #3
>>> "{1} {2} na {0} ka?".format(s1,s2,s3)
'new Year! na Happy ka?'
>>> #4
>>> s2[0]+s1[1:5]+s3[0:4].lower()
'nappyyear'
>>> for i in s1:
	print(i,end=" ")

	
H a p p y 
>>> #Exercises Set B
>>> s1=Happy
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    s1=Happy
NameError: name 'Happy' is not defined
>>> s1="Happy"
>>> s2="New"
>>> s3="Year!"
>>> #1
>>> s1.lower()+s2.lower()+s3[0:4].lower()+"."
'happynewyear.'
>>> #2
>>> s1.replace("H","h")+s2.replace("N","n")+s3.replace("Y","y")
'happynewyear!'
>>> #3
>>> s1.lower()+" "+s2+" "+s3[0:4].upper()+"."
'happy New YEAR.'
>>> #4
>>> [s2,s3,"na",s1,"ka?"]
['New', 'Year!', 'na', 'Happy', 'ka?']
>>> #5
>>> s1.replace("p","r")+" Potter"
'Harry Potter'
>>> 
