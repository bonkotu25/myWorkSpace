import os
import glob
import json

def load_config(config_file):
    with open(config_file, 'r') as file:
        config = json.load(file)
    return config

def update_current_directory(config_file):
    current_directory = os.getcwd()
    print(f"Current Directory before loading config: {current_directory}")  # Add log output here
    with open(config_file, 'r+') as file:
        config = json.load(file)
        config['current_directory'] = current_directory
        file.seek(0)
        json.dump(config, file, indent=4)
        file.truncate()

def aggregate_text_files(folder_path):
    content_yyyy_mm = ""
    content_usage = ""
    
    # Aggregate text from CSV files
    for file in glob.glob(os.path.join(folder_path, '*.csv')):
        if file.endswith('activity.csv'):
            continue
        elif file.split(os.sep)[-1].split('_')[0].isdigit():
            with open(file, 'rb') as f:
                lines = f.read().decode('shift_jis', errors='ignore').splitlines()
                content_yyyy_mm += '\n'.join(lines[1:-1]) + '\n'  # 1行目と最終行を除く
        elif 'ご利用明細' in file:
            with open(file, 'rb') as f:
                lines = f.read().decode('shift_jis', errors='ignore').splitlines()
                content_usage += '\n'.join(lines[7:]) + '\n'  # 1～7行目を除く
                content_usage += '\n'  # 改行を追加
    
    # Save aggregated content to files
    with open(os.path.join(folder_path, 'aggregated_YYYYMM.csv'), 'w', encoding='shift_jis') as f:
        f.write(content_yyyy_mm)
    
    with open(os.path.join(folder_path, 'aggregated_ご利用明細.csv'), 'w', encoding='shift_jis') as f:
        f.write(content_usage)

    print("Files aggregated successfully!")

# Set the path to the config file using __file__
current_dir = os.path.dirname(__file__)
config_file = os.path.join(current_dir, 'config.json')

# Load and update configuration
update_current_directory(config_file)
config = load_config(config_file)

# Print the current directory from config for verification
print(f"Current Directory from config: {config['current_directory']}")

# Call the function with the folder path from the config
aggregate_text_files(config['folder_path'])
