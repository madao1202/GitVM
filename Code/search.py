import os
import pandas as pd
def check_excel_contains_keyword(file_path, keyword):
    try:
        df = pd.read_excel(file_path, sheet_name=None, engine="openpyxl")
        for sheet_name, sheet_data in df.items():
            for row_index, row in sheet_data.iterrows():
                for column_index, cell in row.items():  # Use items instead of iteritems
                    if str(keyword) in str(cell):
                        return f" '{file_path}'里面有'{keyword}', 工作表名'{sheet_name}', 第 ({row_index}行, {column_index}列)"
        return f"'{file_path}检查完毕'"
    except Exception as e:
        return f"Error reading Excel file '{file_path}': {e}"

def search_keyword_in_excel(folder_path, keyword):
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".xlsx") or file_name.endswith(".xls"):
            file_path = os.path.join(folder_path, file_name)
            result = check_excel_contains_keyword(file_path, keyword)
            print(result)

# 示例用法
while True:
    folder_path = input('文件夹路径是：')
    if folder_path.lower() == '退出':
        break
    keyword_to_search = input('要查找的关键词是：')
    if keyword_to_search.lower() == '退出':
        break
    search_keyword_in_excel(folder_path, keyword_to_search)
    print('------------------------')

