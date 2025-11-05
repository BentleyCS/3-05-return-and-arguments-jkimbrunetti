def larger(n1,n2):
    if n1 > n2:
        return n1
    else:
        return n2

def grade(g):
    if g>=90:
        return "A"
    elif g>= 80:
        return "B"
    elif g >= 70:
        return "C"
    elif g >= 60:
        return "D"
    else:
        return "F"

def fizzBuzz(n):
    if n%5==0 and n%3==0:
        return "FizzBuzz"
    elif n%3==0:
        return "fizz"
    elif n%5==0:
        return "buzz"
    else:
        return n

def collatz(n):
    if n==1:
        return n
    if n%2==0:
        return n/2
    else:
        return 3*n+1

def convertTemperature(input):
    if(input[len(input)-1]=="C"):
        input = int(input[0:len(input)-1])
        out = input*(9/5)+32
        return str(int(out))+"F"
    elif(input[len(input)-1]=="F"):
        input = int(input[0:len(input)-1])
        out = (input-32)*5/9
        return str(int(out))+"C"

