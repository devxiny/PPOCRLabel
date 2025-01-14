import os

# 定义输入文件和输出文件的路径
input_file = 'Label.txt'
output_file = 'Label_result.txt'

# 打开输入文件并读取所有行
with open(input_file, 'r') as f:
    lines = f.readlines()

# 过滤掉不存在的路径
filtered_lines = [line for line in lines if os.path.exists("C:\Users\devxiny\Downloads"+line.split()[0])]

# 将过滤后的行写入输出文件
with open(output_file, 'w') as f:
    f.writelines(filtered_lines)

print(f"Filtered paths have been written to {output_file}")