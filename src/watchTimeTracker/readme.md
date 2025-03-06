# watchTimeTracker

**watchTimeTracker**は、配信に訪れた視聴者の視聴データを記録し、視聴時間を追跡するツールです。  
このツールは、視聴者のIDとメッセージ情報を安全に処理し、ログファイルに記録します。

---

## 特徴

- **IDの安全な管理**: 視聴者IDはSHA-256でハッシュ化され、逆変換ができない形でログに保存されます。
- **データの復号化**: Base64形式で暗号化されたデータを復号化してログに出力します。
- **ファイルロック機能**: 複数のプロセスからの同時アクセスを防ぐ安全設計。
- **タイムスタンプ付きログ**: システム時刻とともにデータを記録します。

---

## 必要条件

- Python 3.7以上
- 以下のPythonライブラリ：
  - `filelock`
  - `hashlib`（Python標準ライブラリ）
  - `base64`（Python標準ライブラリ）

インストール:

```bash
pip install filelock
```

### 使い方

#### 1. 実行方法

以下のコマンドを使用してスクリプトを実行します：

```bash
python watchTimeTracker.py <base64_encoded_id> <base64_encoded_message>
```

- `<base64_encoded_id>`: 視聴者IDをBase64で暗号化した値。
- `<base64_encoded_message>`: 視聴者からのメッセージやデータをBase64で暗号化した値。

#### 2. 例

入力:
```bash
python watchTimeTracker.py "MTIzNDU2Nzg5MDEyMzQ1" "SGVsbG8sIFdvcmxkIQ=="
```

出力 (output.txt):
```
20250307T040203,5994471abb01112afcc18159f6cc74b4ad962a6f36f4d4e9448dd3d5825a936d,Hello, World!
```

---

## ファイル構成

- `watchTimeTracker.py`: メインのプログラム。
- `output.txt`: ログファイル。プログラムが生成する実行結果を追記します。

---

## 注意事項

- **データの安全性**: 
  - 視聴者IDはSHA-256でハッシュ化され、逆変換ができない形で保存されます。
  - プライバシー保護のため、ハッシュ化されたIDを使用してログの一貫性を保ちます。
  
- **エラーハンドリング**: 
  - Base64でエンコードされたデータが無効な場合、明確なエラーメッセージが表示されます。
  - 不正な入力に対して適切なフィードバックを提供します。

- **ファイルロック**: 
  - 複数のプロセスから同時にログファイルにアクセスしようとする際の競合を防止します。
  - `filelock`ライブラリを利用し、安全にファイルを扱う設計です。

---

### 4. exeファイルの実行

exeファイルに変換した場合の使い方は下記になります。
`watchTimeTracker.exe`に対して以下のコマンドを参考に実行してください。

```bash
./dist/watchTimeTracker.exe <base64_encoded_id> <base64_encoded_message>
```

- <base64_encoded_id>: Base64でエンコードされた視聴者ID。
- <base64_encoded_message>: Base64でエンコードされた視聴者のメッセージ。  
※たぬえさは自動的にBase64で暗号化してファイルを渡すので明示的に設定する必要はないです。

実行例:

```bash
./dist/watchTimeTracker.exe "MTIzNDU2Nzg5MDEyMzQ1" "5pel5pys"
```

- 第一引数：Base64でエンコードされた視聴者ID「MTIzNDU2Nzg5MDEyMzQ1」（復号化後は「123456789012345」）

- 第二引数：Base64でエンコードされたメッセージ「5pel5pys」（復号化後は「入室」）

出力 (output.txt):

```
20250307T040203,5994471abb01112afcc18159f6cc74b4ad962a6f36f4d4e9448dd3d5825a936d,入室
```

### 最後に
何か不足している点や修正したい部分があれば、いつでも教えてください！
