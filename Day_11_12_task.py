
#TASK 1

#1 Create three variables in a single a line and assign different values to them and make sure their data types are different. Like one is int, another one is float and the last one is a string

x,y,z = ("name",15,18.1)
print(x,y,z)


#2 Create a variable of value type complex and swap it with another variable whose value is an integer.

x=3+5j
y=67
x,y=y,x
print(x)

#3 Swap two numbers using the third variable as the result name and do the same task without using any third variable.

        #First Part
x=14
y=23
tmp=x
x=y
y=tmp
print(x)

        #Second Part
x=14
y=23
x,y=y,x
print(x)


#4 Write a program to print the value given by the user by using both Python 2.x and Python 3.x Version
x=20
print(x)

# ---- to run this in python2, we will go to the terminal and write python, then it will show the python2 version then we will write this code and run it in python2.

#----- to run this in python3, we will follow the same steps mentioned above, but instead of pyhton, we will write python3.

#5 Write a program to complete the task given below:
        #Ask the user to enter any 2 numbers in between 1-10 and add both of them to another variable call z.
        #Use z for adding 30 into it and print the final result by using variable result.

x=int(input("enter first number:(1-10):" ))
if x>10:
    print("enter between 1 to 10")

y=int(input("enter second number:(1-10):" ))
if y>10:
    print("enter between 1 to 10")

z=x+y+30
print(z)


#6 Write a program to check the data type of the entered values. HINT: Printed output should say -  The input value data type is: int/float/string/etc

x=10
print("The input value data type is")
print(type(x))


#7 If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’ again. Will it change the value.

a=10
a="New Value"
print(type(a))



#TASK 2

#If a number is divisible by 3 it should print Consultadd as a string

x=int(input("enter any number: "))
if (x%3==0):
    print("ConsultAdd")
else:
    print("Number is not divisible by 3")


#If a number is divisible by 5 it should print C as a string

x=int(input("enter any number: "))
if (x%5==0):
    print(str("c"))
else:
    print("number is not divisible by 5")

#If a number is divisible by both 3 and 5 it should print Consultadd Python Training as a string.
x=int(input("enter any number: "))
if (x%5==0) and (x%3==0):
    print(str("ConsultAdd Python Training"))

else:
    print("number is not divisible by 3 and 5")


#Write a program in Python to perform the following operator based task:
   #Ask user to choose the following option first:
   #If User Enter 1 - Addition 
   #If User Enter 2 - Subtraction
   #If User Enter 3 - Division
   #If USer Enter 4 - Multiplication
   #If User Enter 5 - Average
   #Ask user to enter the 2 numbers in a variable for first and second for the first 4 options mentioned above.
   #Ask user to enter two more numbers as first1 and second2 for calculating the average as soon as user choose an option 5.


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def average(x, y):
    return (x+y)/2


print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Average")

while True:
    choice = input("Enter choice(1/2/3/4/5): ")

    if choice in ('1', '2', '3', '4', '5'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            result= print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            result= print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            result= print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            result= print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5':
            result= print(num1, "+", num2, "/", 2, "=", average(num1, num2))
        
        if (result<0):
            print("zsa")
        break
        
    else:
        print("Invalid Input")


#Write a program in Python to implement the given flowchart:

a=10
b=20
c=30
avg=(a+b+c)/3
print("avg=", avg)
if(avg>a and avg>b and avg>c):
    print("avg is higher than a,b,c")
else:
    if(avg>a and avg>b):
        print("avg is higher than a,b,c")
    elif(avg>a and avg>c):
        print("avg is higher than a,c")
    elif(avg>b and avg>c):
        print("avg is higher than b,c")
    elif(avg>a):
        print("avg is just higher than a")
    elif(avg>b):
        print("avg is just highr than b")
    elif(avg>c):
        print("avg is just higher than c")


#Write a program in Python to break and continue if the following cases occurs:
        #If user enters a negative number just break the loop and print “It’s Over”
        #If user enters a positive number just continue in the loop and print “Good Going”

while True:
    x= int(input("Enter a number :"))
    if(x<0):
         break
    print("It’s Over")
   

print("Good Going")



#Write a program in Python which will find all such numbers which are divisible  by 7 but are not a multiple of 5, between 2000 and 3200.

for x in range(2000,3200):
    if x%7==0 and x%5!=0:
        print(x)


#What is the output of the following code examples?

#1

x=123
for i in x:
    print(i)

-----> output 
Traceback (most recent call last):
  File "demo1.py", line 206, in <module>
    for i in x:
TypeError: 'int' object is not iterable




#2
i=0
while i<5:
    print(i)
    i+=1
    if i==3:
        break
else:
    print("error")

----> output
0
1
2


#3
count=0
while True:
    print(count)
    count+=1
    if count>=5:
        break

----> output
0
1
2
3
4


#Write a program that prints all the numbers from 0 to 6 except 3 and 6.
       #Expected output: 0 1 2 4 5
       #Note: Use ‘continue’ statement

for x in range(0,6):
    if x==3 or x==6:
        continue
    print(x)


#Write a program that accepts a string as an input from user and calculate the number of digits and letters.
     #Expected output: consul12
     #Letters 6
     #Digits 2

x=input("type a string : ")
letters=0
digits=0
for i in x:
    if i.isdigit():
        digits=digits+1
    elif i.isalpha():
        letters=letters+1
    else:
        pass
print("letters", letters)
print("digits",digits)



# Write a program such that it asks users to “guess the lucky number”. If the correct number is guessed the program stops, otherwise it continues forever. 
#Modify the program so that it asks users whether they want to guess again each time. Use two variables, ‘number’ for the number and ‘answer’ for the answer to the question whether they want to continue guessing. The program stops if the user guesses the correct number or answers “no”. ( The program continues as long as a user has not answered “no” and has not guessed the correct number)

lucky_number=22
answer=0
guess_the_number="yes"
while answer != lucky_number and guess_the_number !="no":
    answer=int(input("Guess the lucky number"))
    if answer != lucky_number:
        print("You have guessed the wrong number")
        guess_the_number = input("try again? Enter yes or no")
print("you won a lottery")




# Write a program that asks five times to guess the lucky number. Use a while loop and a counter, such as
           		#counter=1
		#While counter <= 5:
			#print(“Type in the”, counter, “number”
			#counter=counter+1
    #The program asks for five guesses (no matter whether the correct number was guessed or not). If the correct number is guessed, the program outputs “Good guess!”, otherwise it outputs “Try again!”. After the fifth guess it stops and prints “Game over!”.
    

lucky_number=23
counter=1
while counter<=5:
    
    print("type in the", counter, "number")
    counter=counter+1
    guess=int(input())
    if guess==lucky_number:
        print("Good guess!")
    else:
        print("Try again!")
        
    if counter > 5:
            print("Game over!")


#In the previous question, insert “break” after the “Good guess!” print statement. “break” will terminate the while loop so that users do not have to continue guessing after they found the number. If the user does not guess the number at all, print “Sorry but that was not very successful”.

lucky_number=23
counter=1
while counter<=5:
    
    print("type in the", counter, "number")
    counter=counter+1
    guess=int(input())
    if guess==lucky_number:
        print("Good guess!")
        break
    else:
        print("Try again!")
    
        
    if counter > 5:
            print("Sorry but that was not very successful")

































