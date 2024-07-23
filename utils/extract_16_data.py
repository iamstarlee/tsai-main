import numpy as np
import os
import re

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
                    if "A1\t" in line or "B1\t" in line or "C1\t" in line or "D1\t" in line: 
                        all_data += line + "\n"
        if(i*2 in sensors_list):
            print(f"This is {i*2}")
            with open("/home/whoami/Documents/Hanvon/12种香型白酒/12-2轮复筛-2/20240516/"+file_name, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    if "E1\t" in line or "F1\t" in line or "G1\t" in line or "H1\t" in line: 
                        all_data += line + "\n"
        

    with open("raw_data/dataset/test.txt", 'w') as f:
        f.write(all_data)

if __name__ == '__main__':
    extract_from_files()