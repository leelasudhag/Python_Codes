given a number x = 5 and y = 10. take a number as input and check if the number is in between x, y.

input_number = int(input())
print("given input number is", input_number)
x = 5
y = 10
if input_number > x:
    if input_number < y:
        print("in between " + str(x) + " and " + str(y))
    else:
        print("input_number is greater than " + str(y))
else:
    print("input_number is less than " + str(x))
