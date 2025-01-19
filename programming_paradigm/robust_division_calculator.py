def safe_divide(numerator, denominator):
    try:
        if denominator == 0:
            raise ZeroDivisionError("Division By Zero.")
        elif numerator is str and denominator is str:
            raise ValueError
        else:
            
            return f"he result of the division is {float(numerator)/float(denominator)}"

    except ZeroDivisionError as e:
        print(f"Error: Cannot divide by zero.")

    except ValueError as e:
        print("Error: Please enter numeric values only.")
