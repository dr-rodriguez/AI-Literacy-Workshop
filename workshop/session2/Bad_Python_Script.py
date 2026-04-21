def average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)


def scale(numbers, factor=1):
    for i in range(len(numbers)):
        numbers[i] = numbers[i] * factor
    return numbers


data = []
print("Average:", average(data))

scaled = scale(data)
print("Scaled:", scaled)
