marks = [94.4,65,78,34,67,88,65,69]
print("marks",marks)
print(type(marks))
print(marks[1])

student = ["sharvari",96,20,"chh sambhajinagar"]
print(student[0])
student[0] = "sanjivani"
print(student[0])
print(student)

marks = [10,9,8,4,7]
print(marks[1:4])
print(marks[:4])
print(marks[1:])
print(marks[-3:-1])

list = [2,1,3]
list.append(4)
print(list)

list = [2,1,3]
list.sort()
print(list.sort())
print(list)

list = [2,1,3]
list.reverse()
print(list.reverse())

list= ["banana","leechi","apple"]
print(list.sort(reverse=True))
print(list)

list= ["b","a","c","d","e"]
print(list.sort())
print(list)

list= [2,1,3]
list.insert(1,5)
print(list)

list=[2,3,4,5,6,]
list.pop(3)
print(list)

tuple = (1,2,3,4,5)
print(tuple)
print(type(tuple))

tuple = (1,2,3,4,5)
print(tuple[0])
print(tuple[1])
print(type(tuple))

tup = ()
print(tup)
print(type(tup))

tup=(1,)
print(tup)
print(type(tup))

tup=(1)
print(tup)
print(type(tup))

tup = (1,2,3,4,2,3,2)
print(tup.index(2))
print(tup.count(2))

#movie code
movies = []
mov1=input("Enter 1st movie name: ")
movies.append(mov1)
mov2=input("Enter 2nd movie name: ")
movies.append(mov2)
mov3=input("Enter 3rd movie name: ")
movies.append(mov3)
print(movies)

movies = []
movies.append(input("Enter 1st movie name: "))
movies.append(input("Enter 2nd movie name: "))
movies.append(input("Enter 3rd movie name: "))
print(movies)

#palidrome code
list1 = [1,2,1]
list2 = [1,2,3]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print(" palindrome")
else:
    print("not palindrome")

    #grade code
    
 grade = ("C","D","A","A","B","B","A")
 print(grade.count("C"))