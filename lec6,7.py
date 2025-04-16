'''x = 6
y = "python"
z = 3.4
#print(x)
x = 7
print(x)
print(type(x))
print(type(y))
print(type(z))'''

'''age = "python"
AGE = 16
Age = "java"
print(age)
print(AGE)
print(Age)

age = AGE = Age = ("Java")
print(age)'''

#global_variable : it can be declared out of the variables
'''name = "python" #declaring as global_variable
print("The global variable name is:", name) #accessing an global_variable
name = "java" #modify the global_variable
print("The modified variable name is:", name)'''

'''age = 16
print("My age was:", age)
age = 20
print("My age now is:",age)'''

#string operations
'''Company= "  Wipro   "
print (Company.strip())
print (Company.lstrip())
print (Company.rstrip())
print(Company [0:4] + " " + Company [2:5])'''
#split function
'''a = "hello world, Python is the, good programming language"
b = a.split(" ")
print(b)'''
#count func
'''a = "Python is the, good programming language"
print(a.count('a'))'''

#list
'''lis = ["Python","Java","C++","SQL"]
print(lis)
print(lis[1:3])
print(lis[:-1])
print(lis[:])'''
'''lis2 = ["a","b","c","d","e"]
lis2.extend(lis)
print(lis)'''

#extend and append
'''Lis = [10, 20]
Lis1 = [30, 40]
Lis.extend(Lis1)
print(Lis)
Lis.append(98)
print(Lis)'''

#tuples: datatype which we can't modify
'''tup = (87,98,"java","python",90.4, "python")
print(type(tup))
print(len(tup))
#print(tup[6])
#tup[1]=99 #immutable
#print(tup)
print(tup.count("python"))
print(tup.count("js"))'''

#list comprehension : consize way of writing list
'''lis = [i**2 for i in range(1,10)] #squaring of number from 1 to 10
print(lis)'''

#Dictionary :
'''MNC = {
    "TCS" : 80000,
    "Capgemini" : 270000,
    "Wipro" : 300000,
    "Reliance" : 20000
}
print(MNC["TCS"])
MNC["Google"] = 40000   #adding value
#print(MNC)
#MNC.pop("Wipro")   #removing value
#print(MNC)
#del MNC["Wipro"] #also for removing value
#print(MNC)
MNC["Google"] +=10000
print(MNC)'''

#dictionary comprehension :
'''dic = {i**2 for i in range(1,10)}
print(dic)'''

#set : unorder section of unique items
'''a = {1,2,3,4,5,6}
b = {6,7,8,9,10}
#print(a)
#print(a.intersection(b))
#print(a.union(b))
#print(a-b)
#remove duplicate from set
print(a.union(b)-a.intersection(b))'''

#type conversion
'''a = 45.67
b = float(a)
print(type(b))
c = int(b)
print(type(c))

a = (1,2,3)
b = list(a)
print(b)
print(type(b))'''


#to create a dictionary to check how many funtionalities are in which stage
#1.todo 2.build 3.testing 4.done5.estimation hours(for first functionaltionality is 2 hours)
#how many functionality are there in the 4 stages
#dictionary or any datatype
#{functionality :[stage , estimate time]}
#tthe format {functionality : stage}

'''functionalities = [
    {"name": "Login", "stage": "todo"},
    {"name": "Signup", "stage": "build"},
    {"name": "Profile Update", "stage": "testing"},
    {"name": "Logout", "stage": "done"},
    {"name": "Password Reset", "stage": "build"},
    {"name": "Notifications", "stage": "todo"},
    {"name": "Dashboard", "stage": "done"},
]

stage_counts = {"todo": 0, "build": 0, "testing": 0, "done": 0}

for functionality in functionalities:
    stage = functionality["stage"]
    if stage in stage_counts:
        stage_counts[stage] += 1

total_functionalities = sum(stage_counts.values())

print("Total number of functionalities:", total_functionalities  )'''


#101 - 2 hours and it is To Do stage
#101 - 2 hrs
#To do - 2