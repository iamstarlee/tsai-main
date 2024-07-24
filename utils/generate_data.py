import numpy as np
import sys
import os
from sklearn.model_selection import train_test_split

def generate_data(n = 1):

    # Define the path to your text file
    input_file_path = f'raw_data/day2_dataset/day2_dataset_{n}.txt'

    # Read the file and parse the data into a numpy array
    data = np.loadtxt(input_file_path)

    # Number of rows to select
    rows_per_set = 4

    # Initialize an empty list to store the combinations
    combinations = []

    numbers = 0
    # Nested loops to generate all combinations
    for i0 in range(0, rows_per_set):
        for i1 in range(rows_per_set, 2 * rows_per_set):
            for i2 in range(2 * rows_per_set, 3 * rows_per_set):
                for i3 in range(3 * rows_per_set, 4 * rows_per_set):
                    for i4 in range(4 * rows_per_set, 5 * rows_per_set):
                        for i5 in range(5 * rows_per_set, 6 * rows_per_set):
                            for i6 in range(6 * rows_per_set, 7 * rows_per_set):
                                for i7 in range(7 * rows_per_set, 8 * rows_per_set):
                                    for i8 in range(8 * rows_per_set, 9 * rows_per_set):
                                        for i9 in range(9 * rows_per_set, 10 * rows_per_set):
                                            for i10 in range(10 * rows_per_set, 11 * rows_per_set):
                                                for i11 in range(11 * rows_per_set, 12 * rows_per_set):
                                                    for i12 in range(12 * rows_per_set, 13 * rows_per_set):
                                                        for i13 in range(13 * rows_per_set, 14 * rows_per_set):
                                                            for i14 in range(14 * rows_per_set, 15 * rows_per_set):
                                                                for i15 in range(15 * rows_per_set, 16 * rows_per_set):
                                                                    numbers += 1
                                                                    combination = [
                                                                        data[i0],
                                                                        data[i1],
                                                                        data[i2],
                                                                        data[i3],
                                                                        data[i4],
                                                                        data[i5],
                                                                        data[i6],
                                                                        data[i7],
                                                                        data[i8],
                                                                        data[i9],
                                                                        data[i10],
                                                                        data[i11],
                                                                        data[i12],
                                                                        data[i13],
                                                                        data[i14],
                                                                        data[i15]
                                                                    ]
                                                                    combinations.append(combination)
                                                                    if(numbers == 2000):
                                                                        # Convert combinations to a numpy array
                                                                        combinations = np.array(combinations)

                                                                        # Define the path to save the npy file
                                                                        output_file_path = f'raw_data/day2_dataset/test/test_2000_{n}.npy'

                                                                        # Save the selected combinations to a npy file
                                                                        np.save(output_file_path, combinations)

                                                                        print(f"Top 2000 combinations successfully saved to '{output_file_path}'")
                                                                        sys.exit()

def generate_labels():
    data_list = []
    for i in range(1, 13):
        numbers = np.ones(2000, dtype = int) * i
        data_list.append(numbers)
        # output_file_path = f'raw_data/train_labels_{i}.npy'
        # np.save(output_file_path, numbers)
    concate_data = np.concatenate(data_list, axis=0)
    np.save('raw_data/day2_test_labels_24k.npy', concate_data)
    print(np.load("raw_data/day2_test_labels_24k.npy").shape)
    

def generate_full_data():
    data_list = []
    for i in range(1, 13):
        data_list.append(np.load(f"raw_data/day2_dataset/test/test_2000_{i}.npy"))
    X_train = np.concatenate(data_list, axis=0)

    output_file_path = 'raw_data/day2_test_dataset_24k.npy'
    np.save(output_file_path, X_train)

    print(f"full dataset is {np.load(output_file_path).shape}")


def generate_full_labels():
    data_list = []
    for i in range(1, 13):
        data_list.append(np.load(f"raw_data/day2_dataset/test/test_2000_{i}.npy"))
    X_labels = np.concatenate(data_list, axis=0)

    output_file_path = 'raw_data/test_full_labels.npy'
    np.save(output_file_path, X_labels)

    print(f"full labels are {np.load(output_file_path).shape}")


def split_train_and_test():
    
    # Load the data from a .npy file
    data = np.load('raw_data/day1_full_dataset_12w.npy')
    labels = np.load('raw_data/day1_full_labels_12w.npy')

    # Define the split ratio
    train_ratio = 0.8  # 80% for training, 20% for validation

    # Split the data and labels
    train_data, valid_data, train_labels, valid_labels = train_test_split(data, labels, test_size=(1 - train_ratio), random_state=42)

    # Save the split datasets and labels
    np.save('data/day1_train_data.npy', train_data)
    np.save('data/day1_train_labels.npy', train_labels)
    np.save('data/day1_valid_data.npy', valid_data)
    np.save('data/day1_valid_labels.npy', valid_labels)

    print("Training and validation sets, along with their labels, have been created and saved.")


if __name__ == '__main__':
    pass
    # split_train_and_test()
    # path = "data/day1_valid_data.npy"
    # print(f"Shape of data is {np.load(path).shape}")