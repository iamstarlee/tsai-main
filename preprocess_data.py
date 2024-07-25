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


def substract_and_standardize_number():
    for i in range(1, 13):
        # Open the input file for reading
        with open(f'raw_data/day4_dataset/day4_raw_dataset_{i}.txt', 'r') as input_file:
            lines = input_file.readlines()

        # Open the output file for writing
        with open(f'raw_data/day4_dataset/day4_dataset_{i}.txt', 'w') as output_file:
            for line in lines:
                # Split the line by whitespace to get the first number
                parts = line.split()
                if parts:
                    try:
                        first_number = float(parts[0])  # Convert the first part to a float
                        
                        # Subtract the first number from the rest of the line
                        subtracted_values = [(float(part) - first_number) for part in parts]
                        # Standardization!
                        mean = np.mean(subtracted_values)
                        std_dev = np.std(subtracted_values)
                        subtracted_values = (subtracted_values - mean) / std_dev
                        final_values = [str(values) for values in subtracted_values]

                        # Write the result to the output file
                        output_file.write(' '.join(final_values) + '\n')
                    except ValueError:
                        # Handle cases where the first part is not a valid number
                        print(f"Skipping line: {line.strip()}")

        print(f"Subtraction process completed. Results saved in {i}!")

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
        filename = f'raw_data/three_datasets/train_dataset_{i}.txt'
        
        # Open the file in write mode to create an empty file
        with open(filename, 'w') as file:
            pass  # No content to write, just creating an empty file
        
        # Print confirmation message
        print(f'Created {filename}')

    print("Batch file creation completed.")

def extract_three_datasets():
    for i in range(1, 13):
        # List of input file names
        input_files = [f'raw_data/day1_dataset/day1_dataset_{i}.txt', f'raw_data/day2_dataset/day2_dataset_{i}.txt', f'raw_data/day3_dataset/day3_dataset_{i}.txt']

        # Output file name
        output_file = f'raw_data/three_datasets/train_dataset_{i}.txt'

        # Open output file for writing
        with open(output_file, 'w') as outfile:
            # Loop through each input file
            with open(input_files[0], 'r') as f0:
                lines0 = f0.readlines()

            with open(input_files[1], 'r') as f1:
                lines1 = f1.readlines()

            with open(input_files[2], 'r') as f2:
                lines2 = f2.readlines()

            assert len(lines0) == 64 and len(lines1) == 64 and len(lines2) == 64, "Wrong lines"

            for i in range(0, 64, 4):
                chunk0 = lines0[i:i+4]
                chunk1 = lines1[i:i+4]
                chunk2 = lines2[i:i+4]
                outfile.write(''.join(chunk0))
                
                outfile.write(''.join(chunk1))
                
                outfile.write(''.join(chunk2))
                

        print(f"Data extracted and saved to {output_file}.")


if __name__ == '__main__':
    extract_three_datasets()