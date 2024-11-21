try:
    age = int(input("Enter your age: "))
    print("Age is", age)
    if age % 2 == 0:
        print("The age is even")
    else:
        print("The age is odd")
except ValueError:
    print("Invalid value")
except NameError as UnDefined:
    print("The exception is ",UnDefined)


