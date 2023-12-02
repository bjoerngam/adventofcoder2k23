def calculate_calibration_value(line):
    # Find the first digit
    for char in line:
        if char.isdigit():
            first_digit = int(char)
            break
    else:
        # No digit found at the beginning
        return 0

    # Find the last digit
    for char in reversed(line):
        if char.isdigit():
            last_digit = int(char)
            break

    # Combine the digits to form a two-digit number
    calibration_value = int(str(first_digit) + str(last_digit))

    return calibration_value

def main():

    with open('input.txt') as input_file:
    
            # Calculate calibration values for each line
            calibration_values = [calculate_calibration_value(line) for line in input_file]

            # Sum up the calibration values
            total_calibration = sum(calibration_values)

            # Display the results
            print(f"Total Calibration: {total_calibration}")

if __name__ == "__main__":
    main()
