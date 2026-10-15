# ACCESSING ARRAYS ELEMENTS IN INDEX ( +VE )
fruits = [ "apples" , "mango" , "orange" , "grapes" , "guava"]
print(fruits)
print("length of fruits:", len(fruits))
print(fruits[0])
print(fruits[2])
print(fruits[5-1])


# ACCESSING ARRAYS ELEMENTS IN INDEX ( -VE )
vegatables = [ 'potato' , 'tomato' , 'pumpkin' , 'ladiesfinger' , 'drumstick' ]
print(vegatables)
print("No of vegatables:",len(vegatables))
print(vegatables[-1])
print(vegatables[-1+2])


# FUNCTIONS THE LIST
list=[]
print(list)
list.append("sai")
list.append("ram")
list.append("eswar")
print(list)
list.remove("sai")
print(list)


# UNPACKING THE LIST 
list1 = ["one",2,3,4,5,6,7,"eight",8,9,"10.0"]
print(list1)
one,two,three,*rest=list1
print(one)
print(rest)