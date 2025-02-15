import sys
import base64
import datetime
from filelock import FileLock

def main():
    # 1. 引数チェック
    if len(sys.argv) != 2:
        print("Usage: python script.py <base64_message>")
        sys.exit(1)

    # 2. 引数の復号化
    encoded_message = sys.argv[1]
    decoded_bytes = base64.b64decode(encoded_message)
    user_message = decoded_bytes.decode('utf-8')

    # 3. 文字列生成
    current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    output_string = f"{current_time},{user_message}"

    # 4. ファイルロック
    log_file_path = "output.txt"
    lock_path = log_file_path + ".lock"
    lock = FileLock(lock_path)

    with lock:
        # 5. ファイル出力
        with open(log_file_path, "a", encoding="utf-8") as log_file:
            log_file.write(output_string + "\n")
    
    # 6. ロック解除は自動的に行われます（`with`ステートメント終了時）

if __name__ == "__main__":
    main()
