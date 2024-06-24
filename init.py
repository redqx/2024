import os
import subprocess

def find_and_convert(directory):
    # 遍历目录
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                # 获取 markdown 文件的完整路径
                markdown_file = os.path.join(root, file)
                # 获取文件名并替换扩展名为 .html
                base_name = os.path.splitext(file)[0]
                html_file = os.path.join(root, f"{base_name}.html")

                # 构建 pandoc 命令
                command = f"pandoc --from markdown --to html -o {html_file} --template=bootstrap_menu.html {markdown_file}"
                print(f"Executing command: {command}")

                # 执行命令，忽略输出报错
                subprocess.run(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

# 指定需要遍历的目录
directory_to_search = './2024-year'
find_and_convert(directory_to_search)
