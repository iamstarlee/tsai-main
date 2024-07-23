import numpy as np
import sys

def generate_data():

    # Define the path to your text file
    input_file_path = 'raw_data/train_dataset_3.txt'

    # Read the file and parse the data into a numpy array
    data = np.loadtxt(input_file_path)

    # Number of rows to select from each set of 4 lines
    rows_per_set = 4
    # Total number of sets
    num_sets = 16
    # Number of columns in the dataset
    num_columns = 51

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
                                                                    if(numbers == 10000):
                                                                        # Convert combinations to a numpy array
                                                                        combinations = np.array(combinations)

                                                                        # Define the path to save the npy file
                                                                        output_file_path = 'raw_data/train_10000_3.npy'

                                                                        # Save the selected combinations to a npy file
                                                                        np.save(output_file_path, combinations)

                                                                        print(f"Top 10000 combinations successfully saved to '{output_file_path}'")
                                                                        sys.exit()

def generate_labels(n = 1):
    numbers = np.ones(2000, dtype = int) * 2
    
    output_file_path = 'raw_data/labels2.npy'
    np.save(output_file_path, numbers)

    print(f"np is {np.load(output_file_path)} and shape is {np.load(output_file_path).shape}")
    

def generate_full_data():
    X_train1 = np.load("raw_data/test_2000_1.npy")
    X_train2 = np.load("raw_data/test_2000_2.npy")
    X_train = np.concatenate((X_train1, X_train2), axis=0)

    output_file_path = 'raw_data/test_full_dataset.npy'
    np.save(output_file_path, X_train)

    print(f"full dataset is {np.load(output_file_path).shape}")


def generate_full_labels():
    X_labels1 = np.load("raw_data/labels1.npy")
    X_labels2 = np.load("raw_data/labels2.npy")
    X_labels = np.concatenate((X_labels1, X_labels2), axis=0)

    output_file_path = 'raw_data/test_full_labels.npy'
    np.save(output_file_path, X_labels)

    print(f"full labels are {np.load(output_file_path).shape}")


if __name__ == '__main__':
    generate_data()
