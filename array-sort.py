def get_numbers():
    numbers = []
    for i in range(20):
        while True:
                num = int(input(f"Enter number {i + 1}: "))
                numbers.append(num)
                break
    return numbers

numbers = get_numbers()
sorted_numbers = sorted(numbers)
print("Sorted numbers:", sorted_numbers)
