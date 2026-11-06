def calculate_average(numbers):
    if not numbers:
        return 0

    total = sum(numbers)
    average = total / len(numbers)

    if average > 50:
        print("High average")
    else:
        print("Low average")

    return average


values = [40, 60, 80]

result = calculate_average(values)
print("Average:", result)

assert calculate_average([40, 60, 80]) == 60
assert calculate_average([10, 20, 30]) == 20
assert calculate_average([]) == 0
