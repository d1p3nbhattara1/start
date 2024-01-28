#check out lists and sets in python
#so how does a list work in python:
#well a list is a collection of multiple data of same or different values take a look at the example below

a=["Dipen",18,"ramkot"]

# here a is a list : collection of multiple value that are of different types like string and integer
#to print the whole list just use print(list_name) for an indivual element eg: for 
#first element print[list_name(index)] start woth first item as index 0

print(a)
print(a[0]) # accesing dipen 

print('''

''')
#learning lists function to edit a list like

a.append("ram") # changes name dipen to ram


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

#list methonds
print('''list_name.sort()
         
      use a set for unique elements instead of list 

      
      append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
      

      ''')