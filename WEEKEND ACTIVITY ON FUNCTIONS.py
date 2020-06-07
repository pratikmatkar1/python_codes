#WEEKEND ACTIVITY ON FUNCTIONS

#1 Write a program to reverse a string.
    #Sample data: “1234abcd”
    #Expected Output: “dcba4321”

x="1234abcd" [::-1]
print(x)


#2 Write a function that accepts a string and calculate the number of uppercase letters and lowercase letters.
    #Expected Output:
    #No. of Upper case characters : 3
    #No. of Lower case Characters : 12

def function(x):
    y={"upper case":0, "lower case":0}
    for c in x:
        if c.isupper():
           y["upper case"]+=1
        elif c.islower():
           y["lower case"]+=1
        else:
           pass
    print ("Original String : ", x)
    print ("Total no. of Upper case characters : ", y["upper case"])
    print ("Total no. of Lower case Characters : ", y["lower case"])

function("ConsultAdd BootCamp")


#3 Create a function that takes a list and returns a new list with unique elements of the first list.

def list(l):
    x = []
    for i in l:
        if i not in x:
            x.append(i)
    return x

print(list([1,2,2,4,4,1,1,3,3,3,3,4,5,5,5,3,2,3,2])) 


#4 Write a program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.

items=[n for n in input().split('-')]
items.sort()
print('-'.join(items))

#5 Write a program that accepts a sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

user=input("Please type a sentence : ")

x=user.upper()
print(x)


#6  Define a function that can receive two integral numbers in string form and compute their sum and print it in console.

def find_sum(x,y):
    s=int(x)+int(y)
    return s 

a="10"
b="45"

sum= find_sum(a,b)
print("sum is ",sum)

#7  Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line.
	
def type_a_string(str1, str2):
    if len(str1) == len(str2):
        print(str1+ "\n" + str2)
    else:
        print(max(str1, str2))

type_a_string("Pratik","Matkar")


#8 Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20.

def function():
    l=list()
    for i in range(1,21):
        l.append(i**2)
    print(tuple(l))

function()


#9 Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0 and limit with a label to identify the even and odd numbers. 
    #Example: If the limit is 3 , it should print:
    #  0 EVEN
    #1 ODD
    #2 EVEN
    #3 ODD

limit=int(input("Enter any number between 1 to 50: "))
def showNumbers(limit):
    for i in range(0,limit+1): 
        
        if i%2==0:
            print(i,"even")
           
        elif i%2 !=0:
            print(i,"odd")

showNumbers(limit)


#12 Write a function to compute 5/0 and use try/except to catch the exceptions

def function():
    try:
        x=(5/0)  
        print(x)
    except:
        print("Error with 0")
function()


#13 Flatten the list [[1,2,3].,[4,5],[6,7,8]] into [1,2,3,4,5,6,7,8] using reduce
    #Goal : Turn [1,2,3,4,5,6,7] to 1234567 

lists = [[1, 2, 3], [4, 5], [6, 7, 8]]
new_list = sum(lists, [])
print(new_list)


#14 
def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)


----> output 2











