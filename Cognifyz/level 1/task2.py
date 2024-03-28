def print_pyramid(rows):
    for i in range(1, rows + 1):
        # Print spaces
        for j in range(1, rows - i + 1):
            print(" ", end="")
        
        # Print numbers
        for k in range(1, i * 2):
            print(k, end="")
        
        print()

# Main program
rows = int(input("Enter the number of rows for the pyramid: "))
print_pyramid(rows)
