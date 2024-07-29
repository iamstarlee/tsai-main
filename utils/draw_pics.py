import matplotlib.pyplot as plt
import numpy as np
import re
np.set_printoptions(threshold=np.inf)

def extract_floats(text):
    # 正则表达式模式，用于匹配浮点数
    float_pattern = r'[-+]?\d*\.\d+|\d+'
    
    # 使用re.findall()找到所有匹配的浮点数
    floats = re.findall(float_pattern, text)
    
    # 将匹配到的字符串转换为浮点数
    floats = [float(num) for num in floats]
    
    return floats


if __name__ == '__main__':
    # Define the paths to your text files
    x_file_path = 'raw_data_36sensors/x.txt'
    custom = False
    
    if custom:
        y_file_path = 'raw_data/day2_dataset_1.txt'
        x_coordinates = np.loadtxt(x_file_path)
        y_coordinates = []
        with open(y_file_path, 'r') as f:
            content = f.readlines()
            print(f"Total line is {content.__len__()}")
            for i in range(0, content.__len__(), 8):
                y_coordinates.append(extract_floats(content[i+6])[1:]) # get rid of 1.0
                # print(f"Content is {extract_floats(content[i])[1:]}")

        print(f"y-axis shape is {np.array(y_coordinates).shape}")

    else:
        # Read the x-coordinates from the first file
        x_coordinates = np.loadtxt(x_file_path)

<<<<<<< HEAD
        y_file_path = '/home/whoami/Downloads/train_10000_1.npy'
=======
        y_file_path = 'raw_data_36sensors/y.txt'
>>>>>>> refs/remotes/origin/main
        # Read the 16 sets of y-coordinates from the second file
        # y_coordinates = np.load(y_file_path)[99]
        y_coordinates = np.load(y_file_path)[0]
        print(f"y-axis shape is {y_coordinates.shape}, and x-axis shape is {x_coordinates.shape}")
        

    # Ensure that x_coordinates and y_coordinates have compatible shapes
    # assert np.array(y_coordinates).shape[0] == 16, "The second file must have 16 rows of y-coordinates."

    # Plot the x and y coordinates
    plt.figure(figsize=(10, 6))

    for i in range(np.array(y_coordinates).shape[0]):
        plt.plot(x_coordinates, y_coordinates[i], label=f'Line {i+1}')

    plt.xlabel('X Coordinates')
    plt.ylabel('Y Coordinates')
    plt.title('X and Y Coordinates Plot')
    plt.legend()
    plt.grid(True)
    plt.show()
