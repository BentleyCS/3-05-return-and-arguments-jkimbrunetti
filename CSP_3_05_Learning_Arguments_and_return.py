#Below you will find several older homework questions done correctly using input
#and print statements. our task is to take each one and convert it to arguments and returns instead.


#modify the below function such that it asks the user for 2 numbers as input.
#Then have it print out the larger number
def larger():
    n1 = input("give me a number")
    n2 = input("give me a number")
    n1 = int(n1)
    n2 = int(n2)
    if( n1 > n2):
        print (n1)
    else:
        print (n2)

#Modify the below function such that it asks for the users score as an input.
#Then based on the score print out a letter grade.
# 90+ A
# 80+ B
# 70+ C
# 60+ D
# 59- F
def grade(g):
    g = input("Give me your grade")
    if( g>=90):
        print ("A")
    elif( g>= 80):
        print ("B")
    elif(g >= 70):
        print ("C")
    elif(g >= 60):
        print ("D")
    else:
        print ("F")

#Modify the below function such that it asks the user for a number then
#if the number is divisible by 3 print "fizz"
#if the number is divisible by 5 print "buzz"
#if both are the case then print "Fizzbuzz" instead of the prior two
#if niether are the case print the number.
def fizzBuzz():
    n = input("Give me a number")
    n = int(n)
    if(n%5==0 and n%3==0):
        print( "FizzBuzz")
    elif(n%3==0):
        print ("fizz")
    elif(n%5==0):
        print ("buzz")
    else:
        print(n)

#modify the below function such that it asks the user for an input number.
#if the number is even divide it by two.
#if the number is odd multiply it by 3 and add 1
#then print the new number.
def collatz():
    n = input("Give me a number")
    n = int(n)
    if(n==1):
        print (n)
    if(n%2==0):
        print (n/2)
    else:
        print (3*n+1)





#Modify the below function such that it asks the user for a temperature.
#The format for temperature should end in F For Fahrenheit and C for Celcius
#Then given the temperature if it is in Fahrenheit convert it to Celsius on vice versa
#Example 32F -> 0C  20C -> 68F
def convertTemperature(input):
    #input = input("Give me a temperature")
    if(input[len(input)-1]=="C"):
        input = int(input[0:len(input)-1])
        out = input*(9/5)+32
        print (str(int(out))+"F")
    elif(input[len(input)-1]=="F"):
        input = int(input[0:len(input)-1])
        out = (input-32)*5/9
        print(str(int(out))+"C")

