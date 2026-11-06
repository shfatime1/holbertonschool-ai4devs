# Bug 1: Syntax Error

def calculate_average(numbers):
    total = 0

    for number in numbers:
        total += number

    average = total / len(numbers)
    print("Average:", average)

    if average > 50
        print("High average")
    else:
        print("Low average")

    return average

values = [40, 60, 80]
calculate_average(values)
