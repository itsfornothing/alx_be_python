FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
    celsius = FAHRENHEIT_TO_CELSIUS_FACTOR * (fahrenheit - 32)
    print(f"{fahrenheit} is {celsius}°C")


def convert_to_fahrenheit(celsius):
    fahrenheit = (CELSIUS_TO_FAHRENHEIT_FACTOR * celsius) + 32
    print(f"{celsius} is {fahrenheit}°F")


if __name__ == "__main__":
    temp = float(input("Enter the temperature to convert: "))
    type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

    if type == 'F':
        convert_to_celsius(temp)
    elif type == 'C':
        convert_to_fahrenheit(temp)
    else:
        print("Invalid Input!")
