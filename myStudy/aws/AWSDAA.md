# AWS認定 データエンジニア アソシエイト

- [AWS認定 データエンジニア アソシエイト](#aws認定-データエンジニア-アソシエイト)
  - [Data Pipeline](#data-pipeline)
  - [データパイプラインの流れとAWSサービス](#データパイプラインの流れとawsサービス)
    - [Collection ＆ Ingestion](#collection--ingestion)
      - [Data Type とフォーマット](#data-type-とフォーマット)
      - [データ圧縮](#データ圧縮)
      - [Kinesis](#kinesis)
        - [Amazon Kinesis Data Stream（KDS）](#amazon-kinesis-data-streamkds)
          - [Producer](#producer)
          - [Consumer](#consumer)
        - [キャパシティモード](#キャパシティモード)
        - [特記事項](#特記事項)
        - [よくある問題](#よくある問題)
        - [Amazon Data Firehose（KDF）](#amazon-data-firehosekdf)
          - [KDSとKDFの使い分け](#kdsとkdfの使い分け)
        - [Amazon Managed Service for Apache Flink（旧KDA）](#amazon-managed-service-for-apache-flink旧kda)
      - [DMS](#dms)
      - [SQS](#sqs)
      - [MSK（Amazon Managed Streaming for Apache Kafka）](#mskamazon-managed-streaming-for-apache-kafka)
        - [MSKとkinesisの利用シナリオ](#mskとkinesisの利用シナリオ)
      - [Amazon MQ](#amazon-mq)
      - [AWS Snow Familly](#aws-snow-familly)
      - [AWS Transfer Family](#aws-transfer-family)
      - [AWS DataSync](#aws-datasync)
        - [データ転送サービスの使い分け](#データ転送サービスの使い分け)
      - [AWS DMS（database migration service）](#aws-dmsdatabase-migration-service)
      - [AWS SCT（Schema Conversion Tool）](#aws-sctschema-conversion-tool)
      - [AWS Data Exchange](#aws-data-exchange)
      - [Amazon Appflow](#amazon-appflow)
    - [Strage ＆ Data Management](#strage--data-management)
      - [DATALAKE](#datalake)
      - [S3](#s3)
      - [Lake Formation](#lake-formation)
      - [DWH](#dwh)
      - [Redshift](#redshift)
      - [Data Mart](#data-mart)
      - [RDS](#rds)
      - [Aurora](#aurora)
    - [Processing ＆ Transformation](#processing--transformation)
      - [Glue](#glue)
      - [EMR](#emr)
      - [Kinesis\_](#kinesis_)
      - [Lambda](#lambda)
      - [Step Fanctions](#step-fanctions)
      - [MWAA](#mwaa)
    - [Analysis \& Visualization](#analysis--visualization)
      - [Opensearch](#opensearch)
      - [Redshift\_](#redshift_)
      - [Athena](#athena)
      - [SageMaker](#sagemaker)
    - [Secrity](#secrity)
      - [Artifact](#artifact)
      - [Clowdwatch](#clowdwatch)
      - [Config](#config)
      - [Macie](#macie)
      - [Clowd Trail](#clowd-trail)
      - [IAM](#iam)
      - [KMS](#kms)
      - [VPC](#vpc)

## Data Pipeline

- RawData
  - データ構造
    - 構造化データ
      - 特定のスキーマやフォーマットで構成
      - クエリやスキャンが容易
    - 非構造化データ
      - スキーマや構造を持たない
      - テキスト、電子メール、ﾋﾞﾃﾞｵ、写真など
    - 半構造化データ
      - 構造化データと非構造化データの中間に位置する
      - JSON、XML,特定のNoSQLデータベースなど
  - データ収集のタイミングの違い
    - Batch
      - 一定時間や一定量蓄積したあとにグループ単位でデータを収集・蓄積・処理する方法
      - データは時間をかけて収集され、まとめて処理される。
    - Streaming
      - データが到着または生成サれたときにリアルタイムで処理する方法
      - データは生成または受信された直後に処理される。
- DataLake
  - 構造化データ、半構造化データ、非構造化データに関わらず生データをそのままの形式で保存
  - スケーラビリティに優れている
  - 例：S3、Lakeフォーメーション
- DataWerehouse
  - 特定の目的（レポーティングやデータ分析）に使用されるストレージ
  - 異なるデータソースから統合データを一元的に保管
  - モデル設計
    - StarSchema
      - 中央のfactテーブルと複数のディメンションテーブルで構成される。
      - クエリは単純だが整合性が低い
      - 小規模なデータウェアハウス向け
    - SnoflakeSchema
      - StarSchemaを正規化した形でディメンションテーブルがより分割されている。
      - データの冗長性が減って整合性が向上する。
      - 大規模なデータウェアハウス向け
- DataMart
  - データウェアハウスのサブセット
  - 特定の目的に対応するように設計
  - スキャンするデータ量を制限することでクエリを効率化
- AnalysisVisualization
  - BI（BuisinessIntelligence）
    - 重要なビジネス指標を可視化
  - データ分析
    - 統計的分析、AI・機械学習・深層学習等の手法を使用してデータパターンを分析
- ETL
  - extract(抽出)
    - RDB、基幹システム、フラットファイルなど、様々なソースシステムからデータを抽出
  - transform（変換）
    - 抽出したデータをターゲットとなるデータベースやデータウェアハウスに適した形に変換
    - データのクリーニング、フィルタリング、検証、集計など
  - load（ロード、取り込み）
    - 変換されたデータをデータウェアハウスや他のターゲットシステムにロード

## データパイプラインの流れとAWSサービス

### Collection ＆ Ingestion

#### Data Type とフォーマット

- CSV
  - シンプルで広い用途
  - スキーマがないデータ表現
  - 汎用データ交換に使用
- JSON
  - 軽量なテキストベースのフォーマット
  - 可読性が高く、解析が容易
  - 階層構造やネスト構造を扱う
  - ウェブデータ交換、設定ファイル
- Avro
  - シリアル化とデシリアル化
  - スキーマ駆動型
  - 言語やプラットフォーム間のデータ転送に最適
  - ビッグデータストリーミング
- Parquet
  - ビッグデータ分析に最適化されているカラム型ストレージフォーマット
  - 効率的なデータ圧縮と符号化を提供
  - Hadoopエコシステムとの統合や複雑なネスト構造のサポート
  - 分析処理と大量データ保存
- ORC
  - Optimized Row Colomnar
  - Parquet同様、カラム型ストレージフォーマット
  - 圧縮とパフォーマンスに優れ、主にhadoopエコシステム内で使用
  - 分析処理と大量データ保存

#### データ圧縮

- Gzip
  - 高い圧縮率、ランダムアクセスはサポートされない
  - ファイルサイズの削減が目的のときに使う
- Snappy
  - 列指向ストレージと組み合わせると処理速度向上
  - 圧縮速度が速く、データ分析に適している
  - データのストリーミングや分析でリアルタイム処理が求められる場合に使用
- ZSTD（Zstandard）
  - 高い圧縮率と効率的な圧縮率を両立
  - 大規模データ処理やクラウドサービス
- Bzip2
  - Gzipよりも高い圧縮率だが圧縮と解答が遅い
  - ファイルサイズを重視する長期保存
- LZO
  - 圧縮速度が非常に早いが圧縮率は低め
  - 高速な圧縮/解凍が求められる場面

#### Kinesis

##### Amazon Kinesis Data Stream（KDS）

特徴

- ストリーミングをリアルタイムで収集、処理
- ログ、イベント、市場価格フィード、ソーシャルメディアフィード
- スケーラブルで耐久性に優れたリアルタイムデータストリーミングサービス（サーバーレス）
- 高い耐久性と信頼性：複数AZにレプリケート
- 他サービスとの統合が容易

###### Producer

- ProducerからKinesisへのデータの取り込み
  - プロデューサーからKDSに送信されたレコードはデータブロブとパーティションキーを持つ
  - パーティションキーに基づいてシャードに割り当てて処理をする
  - パーティションキーはハッシュ値を持ちハッシュレンジに基づいてどのシャードに追加するかを決定する。
- RecordPutRate
  - 1秒あたりのレコード書き込み数
  - シャードあたりのレコード数制限は1000レコード
- BytesPutPerShard
  - 1つのシャードに書き込まれるデータ量（秒単位、MB単位）
  - シャードあたりのスループット制限は1MB/秒

ツール

- Kinesis Producer Library（KPL）
  - KDSに効率的にレコードを送信するためのc++/Javaライブラリ
  - AWS SDK for Java 1.Xが必要
  - 特徴
    - 自動再試行
    - 同期と非同期の両方のAPI
    - Cloudwatch メトリクスによるパフォーマンス監視
    - Batch処理により複数レコードをまとめて送信
    - データの自動シャード振り分け
    - データ圧縮
- Kinesis Agent
  - サーバー上でログファイルを監視し、Kinesis Data streamsまたは Data Firehoseに転送する Javaベースのエージェント
  - 特徴
    - 複数のディレクトリとストリーム処理
    - ディレクトリまたはファイルに基づくログルーティング
    - データの前処理（CSVからJSONへの変換など）
    - ファイルのローテーション、チェックポイント、リトライの管理
    - Clowdwatchにメトリクスを送信してモニタリング

###### Consumer

- KinesisからConsumerへのデータ配信
- Amazon kinesis Client library（KCL）を使用することで、複数のシャードから並行してデータを取得可能

ツール

- kinesis Client library（KCL）
  - Kinesis Producer Library（KPL）と併用することでシャード管理を簡素化
  - 複数のConsumerが複数のシャードを共有でき、シャードの探索や負荷分散をサポート
  - DynamoDBを使用してシーケンスやチェックポイントを管理

##### キャパシティモード

| 項目 | Provisionedモード | On-demandモード |
| - | - | - |
| 選択方法 | 手動またはAPIを使用してシャード数をスケール | キャパシティ管理が自動化 |
| Ingress | 1MB/s、1000レコード/s または2MB/s、2000レコード/s | デフォルト容量:4MB/sまたは4000レコード/s |
| Egress | シャードごとに2MB/s | - |
| コスト単位 | シャード数/時間 | データ量（GB/時間） |
| スケーリング基準 |  | 過去30日間で観測されたスループットのピークに基づいてスケール |

##### 特記事項

- 拡張ファンアウト
  - 各コンシューマーはシャードあたり2MB/sの専有スループットを得る
  - 最大20登録でき、総スループットは40MB/s
  - Kinesisはhttp/2を使用してコンシューマーに直接データをプッシュできるようになりレイテンシーが70msに短縮できる。
- クオータ
  - シャード1つあたり1秒あたり最大2MB、2000レコードの取り込み
  - 1秒あたりの取り込み量・読み込み量でシャード数が確定する。リシャーディングも可能
  - データ保持期間は24時間～365日（追加料金）
  - サーバーサイド暗号化をサポート
  - メトリクス・デフォルトでストリーミング単位、追加料金でシャード単位でclowdwatchで監視できる。

##### よくある問題

- ホットシャード
  - 特定のシャードにデータが集中し、スループット制限を超える
    - データを分散するように再設計（パーティションキーにランダムなプレフィックスを付与など）
  - 特定の時間帯にデータが集中、スループット制限を超える
    - データ量が多い時間帯にシャード数を増加させて並列処理させる。
- データ重複
  - Producer側でユニークIDを付与してConsumer側で除去する仕組みが必要
- データの順序が壊れる
  - 同じシャード内では順序性が維持されるが異なるシャードでは維持されない
  - Producer側でシーケンス番号を付与してConsumer側で順序を制御する仕組みが必要。→Consumerの負荷が上がる。

##### Amazon Data Firehose（KDF）

- ストリーミングデータをデータレイクやデータストア、分析ツールに配信する
- ストリーミングデータをキャプチャして変換し、S3、Redshift,OpenSearch Serviceにロード
- フルマネージド型サービス（ユーザー側の管理作業がほぼ不要）
- 自動スケーリング対応
- S3、Redshift、OpenSearch、Splunkに直接送信
- ニアリアルタイムデータ変換、圧縮
  - Lambda関数が組み込まれており、データを変換またはエンリッチ

###### KDSとKDFの使い分け

| 特徴 | KDS | KDF |
| - | - | - |
| カスタマイズ性 | Producer/Consumerの両方 | フルマネージド |
| レイテンシー | リアルタイム | ニアリアルタイム |
| スケーリング管理 | 手動（シャードの分割統合含む） | 自動 |
| データ保管&再生 | 1日から365日まで保管可能 | なし |
| 統合 | Lambdaと連携可能 | Lambdaがネイティブに組み込み |
| 主要用途 | カスタム処理、リアルタイム処理 | S3などの自動化されたフローが必要な場合 |

##### Amazon Managed Service for Apache Flink（旧KDA）

- ストリーミングデータの分析
- Apache Flinkでデータストリームをリアルタイム処理
- レコードはシャード内で24時間から365日間保持（何度でも取得可能）
- フルマネージド
- 高いスケーラビリティ

#### DMS

#### SQS

- フルマネージドのメッセージキューイングサービス
- システム間を疎結合にし、非同期に接続する。
- プロデュサーが大量かつ無規則にメッセージをコンシューマ側に送るとコンシューマがメッセージを処理しきれずにオーバーロードする
- メッセージをキューに入れて待機させることでコンシューマ側の負荷をオフロードする。
- キューポリシー

#### MSK（Amazon Managed Streaming for Apache Kafka）

- AWS環境でApache Kafkaを構築及び実行するフルマネージドサービス
- 大規模ストリーミングデータを高速に処理する分散処理基盤

特徴

- Apache Kafkaクラスタ、Apache ZooKeeper ノードをフルマネージドに管理
- Apache FlinkアプリケーションをAmazon MSK内で実行
- VPCによるネットワーク分離、IAM、データ保管時及び転送時の暗号化
- ブローカーインスタンス、ストレージに基づく従量課金

##### MSKとkinesisの利用シナリオ

- Amazon MSK
  - Apache Kafkaの高度な設定オプションが必要な場合
  - メッセージを長期間保持する必要がある場合
  - 複数の消費者がデータを消費する必要がある場合
- Amazon Kinesis
  - AWSサービスとのネイティブ統合が必要な場合
  - リアルタイム分析（KDA）が必要な場合
  - 短期間のデータ保存が許容可能な場合

#### Amazon MQ

- 異なるシステム間でメッセージを仲介するサービス
- Apache MQ 及び Rabbit MQといった一般的なメッセージキューイングサービスをベースに開発

#### AWS Snow Familly

#### AWS Transfer Family

- SFTP/STPS/STPプロトコルを使ってS3やEFSにデータを転送するサービス
- パブリックなエンドポイント、VPCエンドポイントをサポート
- 各種認証をサポート
  - IAM
  - セッションポリシー
  - ID認証（API Gateway、Active Directory）

#### AWS DataSync

- オンプレミス及び他クラウドとAWS ストレージサービス間のデータを同期的に移行
- NFS、SMBなどのプロトコルやHDFSに対応
- DATASync Agentをソースサーバにインストールし、各種プロトコルと接続

##### データ転送サービスの使い分け

|  | AWS Transfer Family | AWS DataSync | AWS Snow Family |
| - | - | - | - |
| プロトコル | SFTP,FTPS,FTP | NFS,SMB | 物理 |
| 適用例 | - オンラインデータ共有<br>- データアップロード/ダウンロード<br>- レガシーアプリケーションのクラウド移行 | - 大規模なデータセットの移行<br>- 定期的なデータ転送<br>- オンプレからクラウドへのバックアップ | - 膨大なデータ転送が必要<br>インターネット接続が貧弱な場所でのデータ転送 |

#### AWS DMS（database migration service）

- データベースを移行するサービス
- 一括移行及び継続的な差分移行に対応
- 移行タイプ
  - 既存データの移行
  - 既存データを移行して、継続的な変更をレプリケート
  - データ変更のみレプリケート
- 移行状況をモニタリングできる

#### AWS SCT（Schema Conversion Tool）

- 異種のDBMS間のスキーマやビューなどを変換する
- 同種のDBMS間ではAWS DMSや各DBMSの管理ソフトウェアを使用する。
- クライアントOSにインストールして使用する。
- スキーマだけでなくコードオブジェクト（ビュー、ストアド、関数）などをデータベースから読み取り変換する。

#### AWS Data Exchange

- 3rd Partyが提供するデータセットを検索、サブスクライブ、使用できるマーケットプレイス
- データをAPIなどでサブスクライブし、S3に保存したり分析ツールと接続
- 利用料金はデータ提供者とサブスクライバーで異なる。サブスクリプション料金とデータ転送量に対して課金される。

#### Amazon Appflow

- SaasとAWS間を統合しデータ転送を行う
- 特徴
  - フルマネージド
  - セキュリティ：データ転送時、暗号化、IAMによる権限管理に対応
  - 料金：初期費用不要、実行するフロー数と処理されるデータ量に応じて課金

### Strage ＆ Data Management

#### DATALAKE

#### S3

#### Lake Formation

#### DWH

#### Redshift

#### Data Mart

#### RDS

#### Aurora

### Processing ＆ Transformation

#### Glue

#### EMR

#### Kinesis_

#### Lambda

#### Step Fanctions

#### MWAA

### Analysis & Visualization

#### Opensearch

#### Redshift_

#### Athena

#### SageMaker

### Secrity

#### Artifact

#### Clowdwatch

#### Config

#### Macie

#### Clowd Trail

#### IAM

#### KMS

#### VPC


