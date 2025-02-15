# たぬえさ用ロガー

## はじめに

普通につかって！  
引数で連携された内容をexeファイルと同じ場所にそのままtxt出力します。

---
※ここから下は自分用

## ログフォーマット

ログの出力項目は下記  

### 注意事項

- 各項目の間は半角カンマ(,)で区切って出力する。（CSV形式で出力する。）

### ログ形式

| 項番 | 項目       | 桁数 | 内容 | 備考 |
| ---- | ---------- | ---- | ---- | ---- |
| 1   | systemTime   |  -    | yyyymmddhhmmss     |      |
| 2   | type       |  半角2桁    |      |  ※1 後述    |
| 3   | targetID   |   半角25桁   |  対象のIDを格納    |      |
| 4   | targetName |  全角25桁    |   対象の表示名を格納   |      |
| 5   | extendedField1 |   全角25桁   |      |      |
| 6   | extendedField2 |   全角25桁   |      |      |
| 7   | extendedField3 |   全角25桁   |      |      |

※１ typeに格納する値

| トリガー | 格納値       |
| ---- | ---------- |
| レイド   | RD   |
| フォロー   | FO   |
|  チャネポ交換  | CP   |
| オンライン   | ON   |
| オフライン   | OF   |
| 広告スタート   | CS   |
| 広告エンド   | CE   |

## ユースケース

### レイド

| systemTime     | type | targetID                   | targetName                   | extendedField1     | extendedField2 | extendedField3 |
| -------------- | ---- | -------------------------- | ---------------------------- | ------------------ | -------------- | -------------- |
| yyyymmddhhmmss | RD   | レイドしてくださった人のID | レイドしてくださった人の名前 | レイドしてきた人数 |       -        |       -        |

### フォロー

| systemTime     | type | targetID                     | targetName                     | extendedField1 | extendedField2 | extendedField3 |
| -------------- | ---- | ---------------------------- | ------------------------------ | -------------- | -------------- | -------------- |
| yyyymmddhhmmss | FO   | フォローしてくださった人のID | フォローしてくださった人の名前 |      -         |       -        |         -      |

### チャネポ交換

| systemTime     | type | targetID                 | targetName                 | extendedField1       | extendedField2 | extendedField3 |
| -------------- | ---- | ------------------------ | -------------------------- | -------------------- | -------------- | -------------- |
| yyyymmddhhmmss | CP   | 交換してくださった人のID | 交換してくださった人の名前 | 交換されたチャネポ名 | -              | -              |

### オンライン

| systemTime     | type | targetID | targetName | extendedField1 | extendedField2 | extendedField3 |
| -------------- | ---- | -------- | ---------- | -------------- | -------------- | -------------- |
| yyyymmddhhmmss | ON   | 自分のID | 自分の名前 | -              | -              | -              |

### オフライン

| systemTime     | type | targetID | targetName | extendedField1 | extendedField2 | extendedField3 |
| -------------- | ---- | -------- | ---------- | -------------- | -------------- | -------------- |
| yyyymmddhhmmss | OF   | 自分のID | 自分の名前 | -              | -              | -              |

### 広告スタート

| systemTime     | type | targetID | targetName | extendedField1 | extendedField2 | extendedField3 |
| -------------- | ---- | -------- | ---------- | -------------- | -------------- | -------------- |
| yyyymmddhhmmss | CS   | 自分のID | 自分の名前 | -              | -              | -              |

### 広告エンド

| systemTime     | type | targetID | targetName | extendedField1 | extendedField2 | extendedField3 |
| -------------- | ---- | -------- | ---------- | -------------- | -------------- | -------------- |
| yyyymmddhhmmss | CE   | 自分のID | 自分の名前 | -              | -              | -              |

## AP設計

``` mermaid
flowchart TD
  start1([開始])
  node1[引数のチェック]
  node2[引数の復号化]
  node3[文字列生成]
  node4[ファイルのロック]
  node5[ファイル出力]
  end1([終了])
  start1 --> node1 -->　node2 --> node3
  node3 -->　node4 --> node5 --> end1
  node1 --エラーの場合--> end1
```

処理概要：与えられた文字列を同じ階層のテキストファイルに出力するプログラム
入力：文字列（アプリの起動引数で受け取った文字列を想定しています。）
出力：テキストファイル（指定したテキストファイルの最後列に1行追加します。）

処理フロー
1、引数チェック
  引数が渡されているかチェック。なければ処理終了
2、引数の復号化
  引数はbase64で暗号化されているので、復号化する。
3、文字列生成
  システム時刻を取得し、出力文字列を生成する。
4、ファイルロック
  結果出力用テキストファイルのロックを取得
5、ファイル出力
  最後列に生成した文字列を出力する。
6、ロック解除
  ロックを解除する。
