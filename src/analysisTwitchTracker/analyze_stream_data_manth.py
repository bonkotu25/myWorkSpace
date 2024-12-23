import subprocess
import sys
import pandas as pd
import os

# pandasをインストール
subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas"])

import pandas as pd

# 現在の作業ディレクトリを表示
print("Current Working Directory:", os.getcwd())

# カレントディレクトリを変更
os.chdir('d:/github/myWorkSpace/src/analysisTwitchTracker')

# 現在の作業ディレクトリを表示
print("Current Working Directory:", os.getcwd())

# CSVファイルを読み込み
df = pd.read_csv('output_with_all_attributes.csv')

# 'Stream'列をdatetime型に変換
df['Stream'] = pd.to_datetime(df['Stream'])

# 'Month'列を追加
df['Month'] = df['Stream'].dt.to_period('M')

# 分を時間に変換する関数
def minutes_to_hours(minutes):
    return minutes / 60

# 月別でゲームごとの配信時間を集計
monthly_game_hours = df.groupby(['Month', 'Games'])['Duration'].sum().reset_index()
monthly_game_hours['Duration (Hours)'] = monthly_game_hours['Duration'].apply(minutes_to_hours)

# 月ごとの配信時間が多い順にソート
sorted_monthly_game_hours = monthly_game_hours.sort_values(by=['Month','Duration (Hours)'], ascending=False)

# 結果を表示
print("月別でゲームごとの配信時間")
print(sorted_monthly_game_hours[['Month', 'Games', 'Duration (Hours)']])
print("-" * 40)
