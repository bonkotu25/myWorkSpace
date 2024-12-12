import subprocess
import sys
import pandas as pd

# pandasをインストール
subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas"])

import pandas as pd

# CSVファイルを読み込み
df = pd.read_csv('output_with_all_attributes.csv')

# 'Stream'列をdatetime型に変換
df['Stream'] = pd.to_datetime(df['Stream'])

# 分を時間に変換する関数
def minutes_to_hours(minutes):
    return minutes / 60

# RTAと非RTAに分けて1年での総配信時間とRTA時間の計算
attribute_summary = df.groupby('Attribute')['Duration'].sum().reset_index()
attribute_summary['Duration (Hours)'] = attribute_summary['Duration'].apply(minutes_to_hours)
print("RTAと非RTAの総配信時間")
print(attribute_summary[['Attribute', 'Duration (Hours)']])
print("-" * 40)

# ゲームごとに何H遊んだのか
game_hours = df.groupby('Game Genre')['Duration'].sum().reset_index()
game_hours['Duration (Hours)'] = game_hours['Duration'].apply(minutes_to_hours)
print("ゲームごとの総配信時間")
print(game_hours[['Game Genre', 'Duration (Hours)']])
print("-" * 40)

# 欠損値を処理してゲームごとの平均視聴者を計算
df['Viewer Hours'] = df['Avg Viewers'].fillna(0) * df['Duration'].fillna(0) / 60
game_avg_viewers = df.groupby('Game Genre')['Viewer Hours'].sum().reset_index()
game_avg_viewers['Avg Viewers'] = game_avg_viewers['Viewer Hours'] / game_hours['Duration (Hours)']
print("ゲームごとの平均視聴者")
print(game_avg_viewers[['Game Genre', 'Avg Viewers']])
print("-" * 40)

# 時間帯別の視聴者の最小、最大、合計時間の計算
time_period_stats = df.groupby('Time Period').agg(
    Min_Viewers=('Avg Viewers', 'min'),
    Max_Viewers=('Avg Viewers', 'max'),
    Total_Duration=('Duration', 'sum')
).reset_index()

# 合計時間を時間単位に変換
time_period_stats['Total_Duration (Hours)'] = time_period_stats['Total_Duration'].apply(minutes_to_hours)

print("時間帯別の視聴者の最小値、最大値、合計時間")
print(time_period_stats[['Time Period', 'Min_Viewers', 'Max_Viewers', 'Total_Duration (Hours)']])
print("-" * 40)

