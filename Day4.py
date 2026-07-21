info = {
    "key" : "value",
    "name" : "apnacollege",
    "learning" : "coding"
}
print(info)

info = {
    "key" : "value",
    "name" : "apnacollege",
    "learning" : "coding"
}
print(info)

info = {
    "name" : "apnacollege",
    "subject" : ["python","c","java"],
    "topics" : ("dict","set"),
    "age" : 20,
}
print(info)
print(info["name"])
print(info["topics"])

info["name"] = "sharvari dadge"
print(info)

info["name"] = "sharvari"
info["surname"] = "dadge"
print(info)

null_dict = {}
print(null_dict)
null_dict = {}
null_dict["name"] = "apnacollege"
print(null_dict)

student = {
    "name" : "sharu",
    "score" : {
        "chem":98,
        "phy":97,
        "math":95
    }
}
print(student)
print(student["score"])

student = {
     "name" : "rahul kumar",
     "subject":{
         "phy" : 97,
         "chem": 98,
         "math":95
     }
}
print(student.keys())
print(list(student.keys()))
print(list(student.values()))


print(student["name"])
print(student.get("name"))

student = {
     "name" : "rahul kumar",
     "subject":{
         "phy" : 97,
         "chem": 98,
         "math":95
     }
}
print(student.keys())
new_dict = {"city":"delhi",}
student.update(new_dict)
print(student)

 #set
collection = {1,2,3,4}
print(collection)
print(type(collection))


collection = {1,2,3,4,3,"hello","world","world",4}
print(collection)
print(type(collection))
print(len(collection))

collection = set()
collection.add(1)
collection.add(2)
collection.add(3)
collection.add(4)
collection.add("sharvari")
collection.add((1,2,3))#tuple added but cant add list 
collection.remove(3)
print(collection)

collection.clear()
print(len(collection))

collection = {"hello","sharvari","world","beautiful","youre"}
print(collection.pop())
print(collection.pop())
print(collection.pop())\

set1 = {1, 2, 3}
set2 = {2, 3, 4}

print(set1.union(set2))
print(set1.intersection(set2))
#que 1
dictionary = {
    "cat" : "a small animal",
    "table" : ["a pieceof furniture","list of facts & features"]
}
print(dictionary)
#que2
subjects = {
    "python","java","c++","c","javascript"
}
print(subjects)

values = {9, 9.25, 8, 8.0}
print(values)

values = {9, 9.25, 8, "8.0"}
print(values)

values = {
    ("float",9.0),
    ("int",9)
}
print(values)