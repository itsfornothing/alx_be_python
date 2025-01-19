def safe_divide(numerator, denominator):
    try:
        if denominator == 0:
            raise ZeroDivisionError
        elif numerator is str and denominator is str:
            raise ValueError
        else:
            
            return f"The result of the division is {float(numerator)/float(denominator)}"

    except ZeroDivisionError:
        return f"Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."
