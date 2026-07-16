str1='Im sharvari'
str2="im in cse department"
str3='''im in 3rd year'''
print(str1)
print(str2)
print(str3)

str1="sharvari"
str2="dadge"
final_str=str1+str2
print(final_str)

str1="sharvari"
str2="dadge"
final_str=str1+" "+str2
print(final_str)

str3 = "lets"
len3 = len(str3)
print(len3)

str4 = "go"
len4 = len(str4)
print(len4)

final_str = str3+str4
print(final_str)

str = "sharvari"
ch = str[4]
print(ch)
print(str[2:6])
print(str[2:6:2])
print(str[:7])

str= "im studing in cse department"
print(str.upper())
print(str.lower())
print(str.capitalize())
print(str.count("s"))

name = input("Enter your name:")
print("length of your name is",len(name))

str = "Hi, im the $ symbol here $100"
print(str.count("$"))

age = 21

if(age>= 18):
    print("you are eligible to vote")
    print ("you can drive")
elif(age>=16):
    print("you can't vote but you can drive")
else:
    print("you can't vote and you can't drive")

light = "green"

if(light=="green"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("look")

    print("end of code")

marks=80
if(marks>=90):
    grade = "A"
elif(marks>=80 and marks<90):
    grade = "B"
elif(marks>=70 and marks<80):
    grade = "C"
else:
    grade = "D"
print("your grade is",grade)

age=34

if(age>=18):
    if(age>=80):
        print("can not drive")
    else:
        print("can drive")
else:
    print("can not drive")

#oddeven number
num = int(input("Enter a number:"))
if(num%2==0):
    print("even number")
else:
    print("odd number")

#greater number of three numbers
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
num3 = int(input("Enter third number:"))
if(num1>num2 and num1>num3):
    print("greater number is",num1)
elif(num2>num1 and num2>num3):
    print("greater number is",num2)
else:
    print("greater number is",num3)

x = int(input("Enter number:"))

if(x%7 == 0):
    print("multiple of  7")
else:
    print("not multiple of 7")