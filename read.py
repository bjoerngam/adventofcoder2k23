import re

# Use a more descriptive variable name for sum
total_sum = 0

# Updated regular expression to find all consecutive digits in a line
exp = re.compile(r'\d+')

with open('input.txt') as f:
    for line in f:
        # Find all consecutive digits in the line
        digit_groups = exp.findall(line)

        # Extract the first and last digits from each group
        for digit_group in digit_groups:
            if len(digit_group) >= 2:
                first_digit = int(digit_group[0])
                last_digit = int(digit_group[-1])
                two_digit_number = 10 * first_digit + last_digit
                total_sum += two_digit_number

print(total_sum)