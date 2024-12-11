import subprocess
import sys

# beautifulsoup4をインストール
subprocess.check_call([sys.executable, "-m", "pip", "install", "beautifulsoup4"])

# bs4パッケージのBeautifulSoupモジュールをインポート
from bs4 import BeautifulSoup
import csv

# HTMLファイルの読み込み
html_file = 'streams.html'
with open(html_file, 'r', encoding='utf-8') as file:
    html_content = file.read()

# BeautifulSoupでHTMLを解析
soup = BeautifulSoup(html_content, 'html.parser')

# 指定されたテーブルを探す
table = soup.find('table', {'id': 'streams'})

# CSVファイルの作成
csv_file = 'output.csv'
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    for row in table.find_all('tr'):
        csv_row = []
        for cell in row.find_all(['td', 'th']):
            csv_row.append(cell.get_text())
        writer.writerow(csv_row)

print(f"データが {csv_file} に保存されました。")
