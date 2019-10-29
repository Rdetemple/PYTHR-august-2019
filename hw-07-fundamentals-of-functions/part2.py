# Write a FUNction that converts Celsius temperatures to Fahrenheit.
#
# Start with prompting the user for a temperature in Celsius.
#Then call your FUNction and pass in the user input as an argument.
#
# Your FUNction should:
#
# Have one argument: The temperature in Celsius
# Do the conversion with this formula: F = C x 9/5 + 32
# Ensure that the argument you pass in is a number by converting it with int()
temp_number = int(input("Enter temp: "))
def C (Celsius_input):
    F = (Celsius_input * 9/5) + 32
    print(F)

C(temp_number)
