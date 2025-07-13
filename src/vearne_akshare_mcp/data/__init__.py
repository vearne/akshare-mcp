import os
import csv

# 计算data目录的绝对路径
data_dir = os.path.abspath(os.path.dirname(__file__))

def load_code_map():
    """
    Load the US stock code mapping from the CSV file.
    The mapping rules are:
    - Nasdaq → 105.XXXX
    - NYSE → 106.XXXX
    - AMEX → 107.XXXX
    - OTC / Pink Sheets → 153.XXXX
    Example: AAPL -> 105.AAPL
    """
    code_map = {}
    filename = 'us_stock_akshare_codes.csv'
    filepath = os.path.join(data_dir, filename)

    if not os.path.exists(filepath):
        print(f"文件 {filename} 不存在于目录 {data_dir}")
        return code_map

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)  # Skip header row
            for row in reader:
                # Assuming row[1] is the stock symbol and row[4] is the mapped code
                code_map[row[1]] = row[4]
    except Exception as e:
        print(f"加载CSV文件 {filename} 失败: {e}")

    return code_map


code_map = load_code_map()