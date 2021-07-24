#Variables in Python is name for a value

x = 10   #integer
y = 20.2 # float
z = x + y

print(z) # print function

name = "Ramu" # string

#string formatting
# using f string in variable where it helps to embed variables in the string

var1 = f"Hello, {name}"
print(var1)

# another way of string formating
name = "Ramu"
temp = "Hello, {}"
result = temp.format(name)
print(result)
