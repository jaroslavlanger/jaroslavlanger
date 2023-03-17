variable = "var"
var2 = "2"
var3 = 3

print(variable)
print("---")

# No newline at the end
print(variable, end="")
print("---")

# More variables
print(variable, var2, var3)
print("---")

# Different separator
print(variable, var2, var3, sep=", ")
print("---")

# Personal recomendation for var printing (bit advanced, but good practise)
four = 2*2
my_array = [7,"6","five",four,[0,1,2]]
print('"len(my_array[2])": {}'.format(len(my_array[2])))
