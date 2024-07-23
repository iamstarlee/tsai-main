import matplotlib.pyplot as plt
import numpy as np
import re

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
    x_file_path = 'raw_data/x.txt'
    y_file_path = 'raw_data/y.txt'

    custom = True
    if custom:
        x_coordinates = np.loadtxt(x_file_path)
        y_coordinates = []
        for i in range(16):
            
    else:
        # Read the x-coordinates from the first file
        x_coordinates = np.loadtxt(x_file_path)

        # Read the 16 sets of y-coordinates from the second file
        # y_coordinates = np.load(y_file_path)[99]
        y_coordinates = np.loadtxt(y_file_path)
        print(f"y-axis shape is {y_coordinates.shape}")
        

        # Ensure that x_coordinates and y_coordinates have compatible shapes
        assert y_coordinates.shape[0] == 16, "The second file must have 16 rows of y-coordinates."

        # Plot the x and y coordinates
        plt.figure(figsize=(10, 6))

        for i in range(y_coordinates.shape[0]):
            plt.plot(x_coordinates, y_coordinates[i], label=f'Line {i+1}')

        plt.xlabel('X Coordinates')
        plt.ylabel('Y Coordinates')
        plt.title('X and Y Coordinates Plot')
        plt.legend()
        plt.grid(True)
        plt.show()
