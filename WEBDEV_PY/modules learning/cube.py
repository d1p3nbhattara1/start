#importing from the function
from cubefun import  cube


for i in range(10):
    print(f"the cube of {i} is {cube(i)}")

print('''
'''
      
      )

#or 
import cubefun

for i in range(10):
    print(f"the cube of {i+1} is {cubefun.cube(i+1)}")


# to rename a module in a new python file
    #import module_name as new_name

    #some popular module methods are

    print('''
------------------------------------------------
import platform
 x=platform.system()
print (X) : gives what os you are using    
------------------------------------------------   
import platform
 x=dir(platform)
print(x) : returns all the function names (or var name) in a module
------------------------------------------------ 
First module:

   def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}


Second module:

   from mymodule import person1

print (person1["age"])

------------------------------------------------                





------------------------------------------------ 



''')