import subprocess
import sys

# pandasをインストール
subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas"])

import pandas as pd

# CSVファイルを読み込み
df = pd.read_csv('output.csv')

# 列名を表示
print(df.columns)
