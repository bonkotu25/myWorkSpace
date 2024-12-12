import subprocess
import sys

# pandasをインストール
subprocess.check_call([sys.executable, "-m", "pip", "install", "pandas"])

import pandas as pd
from datetime import datetime

# CSVファイルを読み込み
df = pd.read_csv('output.csv')

# 時間帯を判定する関数
def assign_time_period(stream_time):
    try:
        time = datetime.strptime(stream_time, '%Y-%m-%d %H:%M').time()
        if time >= datetime.strptime("06:00", '%H:%M').time() and time < datetime.strptime("12:00", '%H:%M').time():
            return 'Morning'
        elif time >= datetime.strptime("12:00", '%H:%M').time() and time < datetime.strptime("18:00", '%H:%M').time():
            return 'Afternoon'
        else:
            return 'Evening'
    except ValueError:
        return 'Unknown'

# 新しい時間帯列を追加
df['Time Period'] = df['Stream'].apply(assign_time_period)

# 例: 'Title'列を基に属性を付与
def assign_attribute(title):
    if 'RTA' in title:
        return 'Speedrun'
    else:
        return 'Other'

# 新しい属性列を追加
df['Attribute'] = df['Title'].apply(assign_attribute)

# ゲームジャンルを判定する関数
def assign_game_genre(game):
    if pd.isna(game):
        return 'Other'
    game = str(game)
    if 'Harvest Moon' in game or 'Story of Seasons' in game:
        return 'Harvest Moon'
    elif 'Rune Factory' in game:
        return 'Rune Factory'
    elif 'Katamari' in game:
        return 'Katamari'
    elif 'Animal Crossing' in game:
        return 'Animal Crossing'
    elif 'Honkai: Star Rail' in game:
        return 'Honkai: Star Rail'
    elif 'Genshin Impact' in game:
        return 'Genshin Impact'
    elif 'Shepherds Crossing' in game:
        return 'Shepherds Crossing'
    elif 'Pokémon' in game:
        return 'Pokémon'
    elif 'Palworld' in game:
        return 'Palworld'
    else:
        return 'Other'

# 新しいゲームジャンル列を追加
df['Game Genre'] = df['Games'].apply(assign_game_genre)

# 時間帯、属性、ゲームジャンル別に集計
summary = df.groupby(['Time Period', 'Attribute', 'Game Genre']).size().reset_index(name='Count')

# 結果を表示
print(summary)

# 属性付与後のCSVファイルを保存
df.to_csv('output_with_all_attributes.csv', index=False)

print(f"属性付与後のデータが 'output_with_all_attributes.csv' に保存されました。")
