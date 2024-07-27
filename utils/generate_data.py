import numpy as np
import sys
import os
import random
from sklearn.model_selection import train_test_split

def generate_data():
    for n in range(1, 13):
        # Define the path to your text file
        input_file_path = f'raw_data_36sensors/day4_dataset/day4_dataset_{n}.txt'

        # Read the file and parse the data into a numpy array
        data = np.loadtxt(input_file_path)

        # Number of rows to select
        rows_per_set = 4

        # Initialize an empty list to store the combinations
        combinations = []

        numbers = 0
        while(numbers <= 2000):
            numbers += 1
            combination_index = [random.randint(0, 3) for _ in range(36)]
            combination = []
            for i in range(36):
                combination.append(data[combination_index[i] + i * rows_per_set])
            combinations.append(combination)
            if(numbers == 2000):
                # Convert combinations to a numpy array
                combinations = np.array(combinations)

                # Define the path to save the npy file
                output_file_path = f'raw_data_36sensors/three_dataset/test_from_day4/test_2000_{n}.npy'
                
                # Save the selected combinations to a npy file
                np.save(output_file_path, combinations)

                print(f"Top 2000 combinations successfully saved to '{output_file_path}'")
                break


def generate_labels():
    data_list = []
    for i in range(1, 13):
        numbers = np.ones(5000, dtype = int) * i
        data_list.append(numbers)
        # output_file_path = f'raw_data/train_labels_{i}.npy'
        # np.save(output_file_path, numbers)
    concate_data = np.concatenate(data_list, axis=0)
    np.save('data/train_labels.npy', concate_data)
    print(np.load("data/train_labels.npy").shape)
    

def generate_full_data():
    data_list = []
    for i in range(1, 13):
        data_list.append(np.load(f"raw_data_36sensors/three_dataset/train/train_10000_{i}.npy"))
    X_train = np.concatenate(data_list, axis=0)

    output_file_path = 'raw_data_36sensors/full_train_data.npy'
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
    data = np.load('raw_data_36sensors/full_train_data.npy')
    labels = np.load('raw_data_36sensors/labels_12w.npy')

    # Define the split ratio
    train_ratio = 0.8  # 80% for training, 20% for validation

    # Split the data and labels
    train_data, valid_data, train_labels, valid_labels = train_test_split(data, labels, test_size=(1 - train_ratio), random_state=42)

    # Save the split datasets and labels
    np.save('data/train_data.npy', train_data)
    np.save('data/train_labels.npy', train_labels)
    np.save('data/valid_data.npy', valid_data)
    np.save('data/valid_labels.npy', valid_labels)

    print("Training and validation sets, along with their labels, have been created and saved.")


if __name__ == '__main__':
    generate_data()