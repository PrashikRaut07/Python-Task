def calc_area(length, width):
    if length == width:
        return "This is a square"
    elif length * width < 9:
        return "Too small"
    else:
        return length * width

# Get user input
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))

# Call the function and display the result
result = calc_area(length, width)
print("Area:",result)
