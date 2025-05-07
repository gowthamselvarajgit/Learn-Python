# as we receive input from user it can
# only stored as a string not in any other datatype


name = input("Enter Your Name: ")
age = input("How old are you: ")

age = int(age)
age = age + 1

print(f"Hello {name}!")
print(f"You are {age} years old")