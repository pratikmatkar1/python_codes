'''#1 Create a list of the 10 elements of four different types of Data Types like int, string, complex and float.

x=[10,"consultAdd",2+3j,"bootcamp",23.5,"python",22,56,4+5j,33,23]
print(type(x))


#2 Create a list of size 5 and execute the slicing structure

x=[3,4,2,7,5]
x[2:5]
print(x[2:5])

#3 Create a list of given structure and run 
	#x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
    #Access list [1, 2, 3, 4]
    #Access list [600,  700]
    #Access list [100, 300, 500, 600, 800]
    #Access list [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]]
    #Access list [10]
    #Access list [ ]

x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800]
print(x[5][0:4])

print(x[6:8])

print(x[0:9:2])

x.reverse

print(x[5][5][0])

print(x[:])


#4 Create a list of thousand number using range and xrange and see the difference between each other
print(list(range(1,1001)))


#6 Write a program in Python to iterate through the list of numbers in the range of 1,100 and print the number which is divisible by 3 and a multiple of 2.


for i in range(lower, upper+1):
   if((i%3==0) & (i%2==0)):
      print(i)


#7 Write a program in Python to reverse a string and print only the vowel alphabet if exist in the string with their index.

user=input("Please enter any word :")

lis=[]
for i in user:
    if i in "AEIOUaeiou":
        lis.append(i)
   

print(lis)


#8 Write a program in Python to iterate through the string “hello my name is abcde” and print the string which has even length of word.

def function(str):
    result=""
    for i in range(len(str)):   
        if i%2==0:
            result+=str[i]               
    return result

print(function("hello my name is abcde"))


#10 Write a program in Python to complete the following task:
    #Create two different list as in even_list and odd_list
    #Ask user to enter the number in the range of 1,50 and make sure if the entered number is even append it to the even_list and if the entered number is odd append it to the odd list.
    #Keep that in mind you can only add 5 items in each list
    #Make sure once you entered the total 5 element calculate the sum of the list and return the maximum out of the list.

def function(user):
    even=[]
    odd=[]
    for i in user:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    print(even)
    print(odd)

function([4,6,3,8,5,34,65,87,67,86,48,21,37,29,73,] )'''


#12 Generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

x=(1,2,3,4,5,6,7,8,9,10)
list=[]
for i in x:
    if i%2==0:
        list.append(i)
y=tuple(list)
print(y)
print(type(y))





