import os

def filter_existing_files(input_file_path, output_file_path, base_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    existing_lines = []
    for line in lines:
        # 提取文件路径
        parts = line.split()
        if len(parts) > 0:
            file_path = parts[0]
            full_path = os.path.join(base_path, file_path)
            if os.path.exists(full_path):
                existing_lines.append(line)

    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.writelines(existing_lines)

# 使用示例
input_file_path = 'Label.txt'  # 替换为你的输入文件路径
output_file_path = 'Label_result.txt'  # 替换为你的输出文件路径
base_path = 'C:\\Users\\devxiny\\Downloads'  # 替换为你的JPEG文件路径前缀

filter_existing_files(input_file_path, output_file_path, base_path)