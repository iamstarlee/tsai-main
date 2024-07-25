import re
import numpy as np


def extract_floats(text):
    # 正则表达式模式，用于匹配浮点数
    float_pattern = r'[-+]?\d*\.\d+|\d+'
    
    # 使用re.findall()找到所有匹配的浮点数
    floats = re.findall(float_pattern, text)
    
    # 将匹配到的字符串转换为浮点数
    floats = [float(num) for num in floats]
    
    return floats


def average_by_column():
    data = np.loadtxt('raw_data/y_1.txt')

    # Calculate column-wise average
    column_averages = np.mean(data, axis=0).reshape(1, -1)

    # Print the result
    print("Column average:")
    print(column_averages)
    print(f"shape is {column_averages.shape}")
    
    np.savetxt('raw_data/column_average.txt', column_averages)
    print("Column sums saved to 'column_average.txt'.")


def substract_first_number():
    for i in range(1, 13):
        # Open the input file for reading
        with open('raw_data/day1_dataset/day1_raw_dataset_{i}.txt', 'r') as input_file:
            lines = input_file.readlines()

        # Open the output file for writing
        with open('raw_data/day1_dataset/day1_dataset{i}.txt', 'w') as output_file:
            for line in lines:
                # Split the line by whitespace to get the first number
                parts = line.split()
                if parts:
                    try:
                        first_number = float(parts[0])  # Convert the first part to a float
                        print(f"The first number is {first_number}\n")
                        # Subtract the first number from the rest of the line
                        subtracted_values = [str(float(part) - first_number) for part in parts]
                        # Write the result to the output file
                        output_file.write(' '.join(subtracted_values) + '\n')
                    except ValueError:
                        # Handle cases where the first part is not a valid number
                        print(f"Skipping line: {line.strip()}")

        print("Subtraction process completed. Results saved in 'y_1.txt'.")

def test_substract():
    path_file = "raw_data/day1_dataset/day1_dataset_1.txt"
    with open(path_file, 'r') as f:
        line = f.readline().split()
        print(f"line is {line}")
        first_number = float(line[0])
        print(f"first number is {first_number}\n")
        value = [str(float(part) - first_number) for part in line]
        print(f"value is {value}\n")

def transforms():
    path_file = "raw_data/y_1.txt"

    with open(path_file, 'r') as f:
        lines = f.readlines()

    out_path = "raw_data/out_standard.txt"
    with open(out_path, 'w') as f:
        for line in lines:
            data = line.split()
            data = [float(num) for num in data]
            # Calculate mean and standard deviation
            mean = np.mean(data)
            std_dev = np.std(data)

            # Standardize the data
            standardized_data = (data - mean) / std_dev
            for data in standardized_data:
                f.write(str(data)+" ")
            f.write("\n")
            # Print original and standardized data
            # print("Original data:")
            # print(data)
            print("\nStandardized data is saved!")

def build_multiple_files():
    # Number of files to create
    num_files = 12

    # Loop to create each file
    for i in range(1, num_files + 1):
        # Define the filename
        filename = f'raw_data/day4_dataset/day4_dataset_{i}.txt'
        
        # Open the file in write mode to create an empty file
        with open(filename, 'w') as file:
            pass  # No content to write, just creating an empty file
        
        # Print confirmation message
        print(f'Created {filename}')

    print("Batch file creation completed.")


if __name__ == '__main__':
    build_multiple_files()
