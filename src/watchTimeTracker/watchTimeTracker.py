import sys
import base64
import datetime
import hashlib
from filelock import FileLock

def decode_base64(encoded_string):
    """Base64復号化の関数"""
    decoded_bytes = base64.b64decode(encoded_string)
    return decoded_bytes.decode('utf-8')

def hash_id(input_id):
    """IDをハッシュ化する関数（SHA-256を使用）"""
    sha256 = hashlib.sha256()
    sha256.update(input_id.encode('utf-8'))
    return sha256.hexdigest()

def main():
    # 1. 引数チェック
    if len(sys.argv) != 3:
        print("Usage: python script.py <base64_id> <base64_message>")
        sys.exit(1)

    # 2. 第一引数(ID)の復号化とハッシュ化
    encoded_id = sys.argv[1]
    try:
        raw_id = decode_base64(encoded_id)
    except Exception as e:
        print(f"第一引数のBase64復号化中にエラーが発生しました: {e}")
        sys.exit(1)
    
    hashed_id = hash_id(raw_id)

    # 3. 第二引数の復号化
    encoded_message = sys.argv[2]
    try:
        user_message = decode_base64(encoded_message)
    except Exception as e:
        print(f"第二引数のBase64復号化中にエラーが発生しました: {e}")
        sys.exit(1)

    # 4. 文字列生成
    current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    output_string = f"{current_time},{hashed_id},{user_message}"

    # 5. ファイルロック
    log_file_path = "watchTimeTrackerLog.txt"
    lock_path = log_file_path + ".lock"
    lock = FileLock(lock_path)

    with lock:
        # 6. ファイル出力
        with open(log_file_path, "a", encoding="utf-8") as log_file:
            log_file.write(output_string + "\n")
    
    # ロック解除は自動的に行われます（`with`ステートメント終了時）

if __name__ == "__main__":
    main()
