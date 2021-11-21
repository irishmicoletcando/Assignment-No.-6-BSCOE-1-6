# Program 1: Number Sorter
# Create a program that ask 4 numbers. 
# Print the 4 numbers from highest to lowest using only if-else statement.
def ask_num():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        num3 = float(input("Enter third number: "))
        num4 = float(input("Enter third number: "))

    except ValueError:
        print("Enter a number.")

    else:
        # first number
        if num1 > num2 and num1 > num3 and num1 > num4:
            if num2 > num3 and num2 > num4:
                if num3 > num4:
                    descending = num1, num2, num3, num4
                else:
                    descending = num1, num2, num4, num3
                return  descending
            elif num3 > num2 and num3 > num4:
                if num2 > num4:
                    descending = num1, num3, num2, num4
                else:
                    descending = num1, num3, num4, num2
                return descending
            else:
                if num3 > num2:
                    descending = num1, num4, num3, num2
                else:
                    descending = num1, num4, num2, num3
                return descending


descending_order = ask_num()
print(f"Numbers in descending order: {descending_order}")