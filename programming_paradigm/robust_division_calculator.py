def safe_divide(numerator, denominator):
    try:
        if denominator == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero.")
        elif numerator is str and denominator is str:
            raise ValueError
        else:
            
            return f"The result of the division is {float(numerator)/float(denominator)}"

    except ZeroDivisionError as e:
        print(e)

    except ValueError as e:
        print("Error: Please enter numeric values only.")
