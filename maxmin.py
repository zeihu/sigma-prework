def minmax(numbers):
    # initialises minimum and maximum numbers to first item in list
    currentmin = numbers[0]
    currentmax = numbers[0]

    # iterates through list
    for number in numbers:
        # checks if number is smaller than the current minimum, and replaces it if true
        if number < currentmin:
            currentmin = number
        # checks if number is bigger than the current maximum, and replaces it if true
        if number > currentmax:
            currentmax = number

    # returns the minimum and maximum in an array
    return [currentmin, currentmax]


inputnums = input("Enter a list of numbers separated with a space: ")
# converts the numbers from string to integer, and puts them in a list divided by spaces
numbers = [int(num) for num in inputnums.split()]
print(f"Your array: {numbers}")
print("Minimum and maximum values:", minmax(numbers))
