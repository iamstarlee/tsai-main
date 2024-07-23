import numpy as np
import os
import re

# selection from [3,6,10,11,12,13,15,17,21,23,24,26,28,29,32,35]
def preprocess_file():
    file_path = "raw_data/dataset/test_dataset_3.txt"
    with open(file_path, 'r') as file:
        content = file.read()
    
    content = content.replace(',', '')

    with open(file_path, 'w') as file:
        file.write(content)
    print("All commas have been successfully removed.")


def extract_floats(text):
    # 正则表达式模式，用于匹配浮点数
    float_pattern = r'[-+]?\d*\.\d+|\d+'
    
    # 使用re.findall()找到所有匹配的浮点数
    floats = re.findall(float_pattern, text)
    
    # 将匹配到的字符串转换为浮点数
    floats = [float(num) for num in floats]
    
    return floats


def extract_from_files():
    sensors_list = [3,6,10,11,12,13,15,17,21,23,24,26,28,29,32,35]
    
    all_data = ""
    # Get for second day
    for i in range(19):
        file_name = f"05162024_12-3ci-{i}_n001.seq1"
        if(i*2 - 1 in sensors_list):
            print(f"This is {i*2-1}")
            with open("/home/whoami/Documents/Hanvon/12种香型白酒/12-2轮复筛-2/20240516/"+file_name, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    if "A3\t" in line or "B3\t" in line or "C3\t" in line or "D3\t" in line: 
                        str2data = extract_floats(line)[1:]
                        all_data += str(str2data)[1:len(str(str2data))-1] + "\n"
                        
                        
        if(i*2 in sensors_list):
            print(f"This is {i*2}")
            with open("/home/whoami/Documents/Hanvon/12种香型白酒/12-2轮复筛-2/20240516/"+file_name, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    if "E3\t" in line or "F3\t" in line or "G3\t" in line or "H3\t" in line: 
                        str2data = extract_floats(line)[1:]
                        all_data += str(str2data)[1:len(str(str2data))-1] + "\n"
        
    
    with open("raw_data/dataset/test_dataset_3.txt", 'w') as f:
        f.write(all_data)

if __name__ == '__main__':
    preprocess_file()