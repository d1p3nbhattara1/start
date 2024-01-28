#check out lists and sets in python
#so how does a list work in python:
#well a list is a collection of multiple data of same or different values take a look at the example below
a=["Dipen",18,"ramkot"]
# here a is a list : collection of multiple value that are of different types like string and integer
#to print the whole list just use print(list_name) for an indivual element eg: for 
#first element print[list_name(index)] start woth first item as index 0
print(a)
print(a[0]) # accesing dipen 
a2 ={1,2,3} #this is a set and 1,2,3 are set objects
# to access set use the syntax: 

#now let's take a look at object is python

dipen={
    'height':150,
    'name':'ram'
}

print( f"{dipen["height"]} cm") # accessing the elements of an object
print(dipen)
print(dipen['name'])

#now making a dictionary use dict {"key values : take it as like real dict" , call the key-value pair}

