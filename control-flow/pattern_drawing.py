length = int(input("Enter the size of the pattern: "))

i = 0

while i <= length:
    for j in range(1,length+1):
        print("*", end="")

    i+=1
    print("\n")