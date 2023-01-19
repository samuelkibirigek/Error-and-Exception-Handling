#Exception Handling

#try means this block of code could cause an exception aka error
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])

#except tells the program what to do in the case try has an exception or error
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")

#you can have multiple except blocks of code each for specific errors as shown
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")

#else defines a block of code to be run in case try returns no exceptions
else:
    content = file.read()
    print(content)

#finally is used to define code that should be run no matter what happens
finally:
    raise TypeError("This is an error that I made up.")

#raise keyword allows for a specific error to be reported and it can take a string parameter
#that specifies exactly what to be reported as shown.
# See BMI Example





