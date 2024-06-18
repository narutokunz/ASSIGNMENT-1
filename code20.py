def calculate_sum(numbers):
    
    total_sum = 0

    for num in numbers:
        total_sum += num

    return total_sum

input_numbers = input("Enter numbers separated by spaces:")
numbers_list = list(map(int, input_numbers.split()))


sum_of_numbers = calculate_sum(numbers_list)

print(f"The sum of the numbers is: {sum_of_numbers}")
