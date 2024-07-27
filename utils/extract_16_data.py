import numpy as np
import os
import re

# selection from [3,6,10,11,12,13,15,17,21,23,24,26,28,29,32,35]
def preprocess_file():
    for i in range(1,13):
        file_path = f"raw_data_36sensors/day1_dataset/day1_dataset_{i}.txt"
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

def rename_files():
    dir_name = "raw_data/day4_dataset"
    for filename in os.listdir(dir_name):
        
        if filename.endswith('.txt') and filename.startswith('day4_dataset_'):
            number = filename.split('_')[2].split('.')[0]

            new_filename = f'day4_raw_dataset_{number}.txt'
            old_file = os.path.join(dir_name, filename)
            new_file = os.path.join(dir_name, new_filename)

            # Rename the file
            os.rename(old_file, new_file)
            print(f'Renamed: {filename} to {new_file}')

def extract_from_16files():
    sensors_list = [3, 6,10,11,12,13,15,17,21,23,24,26,28,29,32,35]
    
    for j in range(1, 13):
        all_data = ""
        # Get for first day
        for i in range(1,19):
            file_name = f"05222024_12-5ci-{i}_n001.seq1"
            if(i*2 - 1 in sensors_list):
                with open("/data/lxx/Download/12种香型白酒/12-2轮复筛-4/20240522/"+file_name, 'r') as f:
                    lines = f.readlines()
                    for line in lines:
                        if f"A{j}\t" in line or f"B{j}\t" in line or f"C{j}\t" in line or f"D{j}\t" in line: 
                            str2data = extract_floats(line)
                            str2data = [num for num in str2data if num > 13.0]# 去掉所有个位浮点数
                            assert np.array(str2data).shape[0] == 70, "The columns must be 70."
                            all_data += str(str2data)[1:len(str(str2data))-1] + "\n"
                            
                            
            if(i*2 in sensors_list):
                with open("/data/lxx/Download/12种香型白酒/12-2轮复筛-4/20240522/"+file_name, 'r') as f:
                    lines = f.readlines()
                    for line in lines:
                        if f"E{j}\t" in line or f"F{j}\t" in line or f"G{j}\t" in line or f"H{j}\t" in line: 
                            str2data = extract_floats(line)
                            str2data = [num for num in str2data if num > 13.0]# 去掉所有个位浮点数
                            assert np.array(str2data).shape[0] == 70, "The columns must be 70."
                            all_data += str(str2data)[1:len(str(str2data))-1] + "\n"
            
        
        with open(f"raw_data/day4_dataset/day4_dataset_{j}.txt", 'w') as f:
            f.write(all_data)
        print(f"Success for the {j}!")

def extract_from_36files():
    for j in range(1, 13):
        all_data = ""
        for i in range(1,19):
            file_name = f"05222024_12-5ci-{i}_n001.seq1"
            with open("/data/lxx/Download/12种香型白酒/12-2轮复筛-4/20240522/"+file_name, 'r') as f:
                lines = f.readlines()
                for line in lines:
                    if f"A{j}\t" in line or f"B{j}\t" in line or f"C{j}\t" in line or f"D{j}\t" in line or\
                        f"E{j}\t" in line or f"F{j}\t" in line or f"G{j}\t" in line or f"H{j}\t" in line:
                        str2data = extract_floats(line)
                        str2data = [num for num in str2data if num > 13.0]# 去掉所有个位浮点数
                        assert np.array(str2data).shape[0] == 70, "The columns must be 70."
                        all_data += str(str2data)[1:len(str(str2data))-1] + "\n"
        
        with open(f"raw_data_36sensors/day4_dataset/day4_dataset_{j}.txt", 'w') as f:
            f.write(all_data)
        print(f"Success for the {j}!")


if __name__ == '__main__':
    preprocess_file()