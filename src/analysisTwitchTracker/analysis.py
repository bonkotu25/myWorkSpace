import subprocess
import sys
from datetime import datetime, timedelta

# beautifulsoup4をインストール
subprocess.check_call([sys.executable, "-m", "pip", "install", "beautifulsoup4"])

# bs4パッケージのBeautifulSoupモジュールをインポート
from bs4 import BeautifulSoup
import csv

# HTMLファイルの読み込み
html_file = 'sample.html'
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
    
    # ヘッダー行を処理
    header = table.find('thead').find_all('th')
    csv_header = [th.get_text().strip() for th in header]
    writer.writerow(csv_header)
    
    # ボディ行を処理
    for row in table.find('tbody').find_all('tr'):
        csv_row = []
        for cell in row.find_all(['td', 'th']):
            # <span>タグの中のテキストを抽出
            if cell.find('span'):
                text = cell.find('span').get_text()
            else:
                text = cell.get_text().strip()
            # 改行をスペースに置き換え
            text = text.replace('\n', ' ').replace('\r', '').strip()
            text = ' '.join(text.split())
            if cell == row.find_all(['td', 'th'])[0]:
             try:
                utc_time = datetime.strptime(text, '%Y-%m-%d %H:%M')
                jst_time = utc_time + timedelta(hours=9)
                text = jst_time.strftime('%Y-%m-%d %H:%M')
             except ValueError:
                pass
            csv_row.append(text)
        writer.writerow(csv_row)

print(f"データが {csv_file} に保存されました。")
