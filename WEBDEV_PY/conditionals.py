#checking out conditional flow of python program
#input function always returns string data type
n=int(input("number: "))
if n > 0:
    print(f"{n}, is greater than zero i.e. positive")
elif n < 0:
      print(f"{n}, is lesser than zero i.e. negative")
else:
    print("the number you entered is 0")

