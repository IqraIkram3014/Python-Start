# Example of variable and output 
""" name = "Tony Shark"
age = '51'
is_genius = True
print (name, 'is' ,age, 'years old man and genius', is_genius) """

#input from user Catcatenation short exercise
""" Superhero = input("Who is you favourite superhero? ")
print("My superhero is " + Superhero) """

#Type Conversion (Means our input normally takes string and also frint string)
#it will give error if with give int it visulize str so we do type conversion
#by using function int(age), float(), str(), bool()

#practice question to print sum of 2 numbers
""" first = input("Enter first number")
Second = input("Enter sec number")
sum = int(first) + int(Second)
print("the sum is: " + str(sum)) """


#Strings
""" name = "Iqra"
print(name.upper())
print(name.find('I')) #if this find the charcter it will return char's index like I on 0, if it has not have char it will return -1
print(name.replace("Iqra", "Jannat")) """


#Keywords
#highted words
""" name="iqra"
print("i" in name) # in can return what we search in string
 """


#Arithmetic Operations (+,-,*,/,// for prevent float num, %, for power**)
#Shortcuts  i+=2 > i =i +2
# precedence ()->*,/ ->  

#Comparison Operators
""" print(3<2)
print(3>2)
print(3>=2)
print(3 == 2)
print(3!=2) """


#Logical Opeartors (or, and,not )
""" print(2>3 or 2<3)
print (3>2 and 2>1)
print(not 3>2) """

#Conditions  
""" age =22
if age >= 18: #for block of code
    print("You are an adult")
    print("You can vote")
elif age < 18 and age > 3:
    print("You are in school")
else:
    print("You are child")

print("Thank you") """


#Mini Calculator Project

""" first = input("Enter first number : ")
operator = input("enter oprator(+,-,*,/,%) : ")
second = input("Enter second number : ")
first = int(first)
second = int(second)
if operator == "+":
    print (first + second)
elif operator == "-":
    print (first - second)
elif operator == "*":
    print (first * second)
elif operator == "/":
    print (first / second)
elif operator == "%":
    print (first % second)
else:
    print("Invalid Operator") """


""" #Range (from this value to end)
num = range(6)
print(num)
 """
#Loops
""" i = 5
while i >=0:
    print(i * '*')
    i = i - 1 """
""" 
i = 0
while i <+ 5:
    print(i * '*')
    i = i + 1 """

""" for items in range(14):
    print (items + 1) """

#List
""" marks = [23,45,55]
print(marks) """


#Math Module inbuilt
""" from math import *
print(sqrt(4)) """


# Function
""" def sum(first, second):
    print(first + second)


sum(14,30) """