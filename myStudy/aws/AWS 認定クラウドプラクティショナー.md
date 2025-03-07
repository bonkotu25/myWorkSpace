# AWS 認定クラウドプラクティショナー

- [AWS 認定クラウドプラクティショナー](#aws-認定クラウドプラクティショナー)
  - [AWSのセキュリティ](#awsのセキュリティ)
    - [IAM](#iam)
      - [IAMユーザーグループ](#iamユーザーグループ)
      - [IAMロール](#iamロール)
    - [セキュリティグループ](#セキュリティグループ)
      - [デフォルトのセキュリティグループ](#デフォルトのセキュリティグループ)
    - [AWS Shield](#aws-shield)
    - [AWS WAF](#aws-waf)
    - [inspector](#inspector)
    - [AWS Artifact](#aws-artifact)
    - [AWS Key Management Service(KMS)](#aws-key-management-servicekms)
  - [AWSのテクノロジー](#awsのテクノロジー)
  - [AWSのコンピューティングサービス](#awsのコンピューティングサービス)
    - [コンテナ](#コンテナ)
      - [ECS](#ecs)
      - [Amazon EKS](#amazon-eks)
    - [Lightstail](#lightstail)
    - [Batch](#batch)
    - [EC2](#ec2)
      - [EC2のインスタンス](#ec2のインスタンス)
      - [プレイスメントグループ](#プレイスメントグループ)
      - [AutoScaling](#autoscaling)
      - [Amazon Machine Image (AMI)](#amazon-machine-image-ami)
    - [ELB](#elb)
      - [スティッキーセッション](#スティッキーセッション)
    - [Auto Scaling](#auto-scaling)
    - [Lambda](#lambda)
  - [AWSのストレージサービス](#awsのストレージサービス)
    - [ストレージの種類](#ストレージの種類)
    - [EFS](#efs)
      - [マウントターゲット](#マウントターゲット)
    - [Storage Gateway](#storage-gateway)
    - [EBS](#ebs)
      - [EBSのRAID構成](#ebsのraid構成)
    - [S3](#s3)
      - [S3の容量制限](#s3の容量制限)
      - [S3の整合性モデル](#s3の整合性モデル)
      - [S3のセキュリティ](#s3のセキュリティ)
      - [S3の料金について](#s3の料金について)
      - [S3のタイプ](#s3のタイプ)
      - [ライフサイクル管理](#ライフサイクル管理)
      - [S3の特殊な機能](#s3の特殊な機能)
    - [S3のアクセス管理](#s3のアクセス管理)
    - [Amazon S3 Transfer Acceleration](#amazon-s3-transfer-acceleration)
    - [マルチパートアップロード API](#マルチパートアップロード-api)
    - [Snowball](#snowball)
    - [AWS Snowball Edge](#aws-snowball-edge)
  - [ネットワークサービス](#ネットワークサービス)
    - [VPC](#vpc)
    - [サブネット](#サブネット)
  - [インターネットゲートウェイ](#インターネットゲートウェイ)
    - [インターネットゲートウェイの目的](#インターネットゲートウェイの目的)
    - [ルートテーブル](#ルートテーブル)
    - [ネットワークACL](#ネットワークacl)
    - [外部からEC2インスタンスにアクセスするには](#外部からec2インスタンスにアクセスするには)
    - [ハイブリッド構成環境](#ハイブリッド構成環境)
  - [カスタマーゲートウェイ](#カスタマーゲートウェイ)
  - [CloudFront](#cloudfront)
  - [データベースサービス](#データベースサービス)
    - [RDS](#rds)
    - [DynamoDB](#dynamodb)
  - [管理サービス](#管理サービス)
    - [Cloudwatch](#cloudwatch)
    - [Trusted Advisor](#trusted-advisor)
  - [料金と請求](#料金と請求)
  - [AWS Database Migration Service （DMS）](#aws-database-migration-service-dms)
  - [AWS Application Discovery Service](#aws-application-discovery-service)
  - [AWS CloudTrail](#aws-cloudtrail)
  - [Amazon SNS](#amazon-sns)
  - [Amazon SES](#amazon-ses)
  - [Amazon SQS](#amazon-sqs)
  - [Amazon MQ](#amazon-mq)
  - [Amazon RDS](#amazon-rds)
    - [RDSプロキシ](#rdsプロキシ)
  - [Amazon Aurora](#amazon-aurora)
  - [Amazon DynamoDB](#amazon-dynamodb)
    - [DynamoDBストリーム](#dynamodbストリーム)
  - [Amazon Redshift](#amazon-redshift)
    - [Amazon Redshift Spectrum](#amazon-redshift-spectrum)
  - [Amazon EMR](#amazon-emr)
  - [AWS Organizations](#aws-organizations)
  - [メモ](#メモ)
    - [覚えておくべき移行関連のAWSサービス](#覚えておくべき移行関連のawsサービス)
    - [比較](#比較)
    - [AWSでセキュリティを向上させる](#awsでセキュリティを向上させる)
    - [AWSの可用性について](#awsの可用性について)
    - [ACLとセキュリティグループの違い](#aclとセキュリティグループの違い)
    - [AWSのモニタリング系サービス](#awsのモニタリング系サービス)
    - [AWS SDK](#aws-sdk)
    - [AWS プロフェッショナルサービス](#aws-プロフェッショナルサービス)
    - [Route53](#route53)
      - [位置情報ルーティング](#位置情報ルーティング)
    - [AWS OpsWorks](#aws-opsworks)
    - [AWS Elastic Beanstalk](#aws-elastic-beanstalk)
    - [AWS CloudFormation](#aws-cloudformation)
    - [Elasticache](#elasticache)
    - [コード関連のサービス](#コード関連のサービス)
    - [Amazon Neptune](#amazon-neptune)
    - [AWS Security Token Service (AWS STS)](#aws-security-token-service-aws-sts)
    - [Amazon Cognito](#amazon-cognito)
    - [Amazon Elastic Container Registry (ECR)](#amazon-elastic-container-registry-ecr)
    - [Amazon Kinesis](#amazon-kinesis)
      - [Amazon Kinesis Data Streams](#amazon-kinesis-data-streams)
      - [Amazon Kinesis Data Firehose](#amazon-kinesis-data-firehose)
      - [Amazon Kinesis Data Analytics](#amazon-kinesis-data-analytics)
      - [Kinesis クライアントライブラリ (KCL)](#kinesis-クライアントライブラリ-kcl)
    - [Amazon API Gateway](#amazon-api-gateway)
    - [VPCエンドポイント](#vpcエンドポイント)
    - [AWS Certificate Manager](#aws-certificate-manager)
    - [AWS Nitro Enclaves](#aws-nitro-enclaves)
    - [S3のイベント通知](#s3のイベント通知)
    - [Amazon EventBridge](#amazon-eventbridge)
    - [AWS Glue](#aws-glue)
      - [AWS Glue データカタログ](#aws-glue-データカタログ)
    - [AWS ParallelCluster](#aws-parallelcluster)
    - [AWS Secrets Manager](#aws-secrets-manager)
    - [Amazon Data Lifecycle Manager](#amazon-data-lifecycle-manager)


## AWSのセキュリティ

- AWSはクラウド本体のセキュリティ部分を担当し、ユーザーはクラウド内のセキュリティを担当する。（クラウドセキュリティ責任分担モデル）
- EC2やVPCなど、IaaSのカテゴリーに分類されるAWS製品はユーザーがすべて管理するため、必要なセキュリティ設定と管理タスクをすべて実行する必要がある。
- AWSはユーザーがクラウドにおけるセキュリティ対策を行う上で便利なツールやサービスを提供する。
- AWS セキュリティには、データ保護、コンプライアンス要件への準拠、コスト削減、迅速なスケーリングという4つの利点がある。

### IAM

#### IAMユーザーグループ

- ユニットとして管理されるIAMユーザーのコレクションです。 グループを使用すると、複数のユーザーの権限を指定できるため、ユーザー権限を管理しやすくなります

#### IAMロール

- AWSリソースに対してアクセス権限を付与する方法

### セキュリティグループ

- セキュリティグループはEC2インスタンスやDBインスタンスなどのインスタンスの通信トラフィックを制御するファイアウォール。
- セキュリティグループはHTTPやSSHなどのプロトコルを指定して通信を許可する設定を行うことができる。  
- VPC内でインスタンスを立ち上げた場合、1つのインスタンスに対して同時に最大５つまでのセキュリティグループを設定することができる。

#### デフォルトのセキュリティグループ

デフォルトではセキュリティグループは下記のように設定されている。

- インバウンド
  - セキュリティグループ内から全て
- アウトバウンド
  - すべてのIpv4トラフィック

### AWS Shield

- Ddos攻撃に対する保護サービス
- AWS Shield Standardじゃ一般的なDDos攻撃から市捨てmを保護する。
- AWS Shield AdvancedはStandardに加えてDDOS Response Teamによる緩和策を実施し、攻撃を可視化する。
- AWS Shield AdvancedではAWS WAFが無償で無制限に利用可能

### AWS WAF

- AWSが提供するマネージド型のWAF
- AWS WAFの基本料金は無料。webセキュリティルールに基づいて課金される。
- AWS WAFのセキュリティルールはユーザーが設定する必要がある。
- Web ACL の適用サービスはCloudfront、ALB、API gateway、AWS Appsync、Amazon Cognitoから選択する。
- Web ACLを使用して特定エリアからのアクセスを遮断できる

### inspector

- 脆弱性診断を自動で行うことができる。
- EC2上にデプロイされたアプリケーションに対応
- 各種ルールパッケージはAWSが最新のものにアップデート
- スケジューリング設定により完全に自動でチェック可能

### AWS Artifact

- AWSのコンプライアンスレポートにオンデマンドでアクセスできる。
- Service Organization Control(SOC)、Payment Card Industry(PCI)レポートなどが取得可能

### AWS Key Management Service(KMS)

- AWS上で暗号化のためのキーを作成・管理し・暗号化の制御が行えるサービス

---

## AWSのテクノロジー

- リージョンにはアベイラビリティゾーンが2つ以上ある。
- AZは障害が同時に影響しないよう、地理的に十分に離れた場所にある。
- 同一リージョン内のAZ同士は高速なプライベート光ファイバーネットワーキングで接続されている。
- 複数のAZを使うことで耐障害性、可用性の高いアーキテクチャを実装できる。
- DCはセキュリティ、コンプライアンス上の様々な第三者監査検証を実施している。
- エッジロケーションはリージョンとは違う場所に全世界で200か所以上ある。
- エッジロケーションではAmazon Route53が利用され、これによって低レーテンシーなDNSクエリが実現される。
- エッジロケーションではAmazon CroudFrontが利用され、これによってコンテンツの低レイテンシーな配信が実現される。

## AWSのコンピューティングサービス

### コンテナ

#### ECS

- 「Amazon Elastic Container Service」の略。コンテナ管理を行う。
- 起動タイプ
  - ECS起動タイプ
    - サーバータイプ
  - Fargate起動タイプ
    - サーバレスで実行可能
    - ユーザー側でサーバータイプの選択、クラスターをスケールするタイミングの決定、クラスターのパッキングの最適化を行う必要がない

#### Amazon EKS

kubernetesと呼ばれる形式のコンテナー仮想化を実現する

### Lightstail

- AWSが提供する仮想プライベートサーバー

### Batch

- フルマネージド型のバッチ処理実行環境

### EC2

- 必要な時に必要なだけのEC2インスタンスを使用できる
- 必要なEC2インスタンスの数を予測する必要はない
- 運用を開始した後に柔軟に性能を変更できる
- 必要なEC2インスタンスの性能を性能を予測する必要がない
- 使った分にだけ時間単位/秒単位の料金が発生する。
- アウト通信に転送料金が発生する。
- 数分でEC2を世界中で起動できる。
- AMIから同じ構成のEC2インスタンスを難題でも起動できる
- EC2インスタンスへのトラフィックはセキュリティグループのインバウンドで制御する。
- オペレーティングシステムの管理者はキーペアで安全にログインし、root権限、admin権限を持つ
- ユースケースに応じて料金オプションを使い分けることでコスト効率が向上する。

#### EC2のインスタンス

1. オンデマンドインスタンス
    - 通常の購入方式
2. リザーブドインスタンス
    - 1年もしくは3年の期間契約
    - リザーブドインスタンスマーケットプレイス
3. スポットインスタンス
    - オンデマンドよりも低価格で利用できる。実行時間に柔軟性がある場合や中断できる処理に利用する。
4. スケジュールドリザーブドインスタンス
    - 2021年に廃止

#### プレイスメントグループ

単一のAZ内のインスタンスのパフォーマンスを向上させるために論理的にグループ化する機能

- クラスタープレイスメントグループ
  - 単一のAZ内のインスタンスのパフォーマンスを向上させるために論理的にグループ化する機能
  - 同一リージョン内の複数のピアVPCにまたがることも可能
  - グループ内のインスタンスはTCP/IPチラフィックのフローあたりのスループット上限が高くなり、インスタンス間の通信が向上する。
  - 低いネットワークレイテンシー、高いネットワークスループットを実現する。
- パーティションプレイスメントグループ
  - EC2は各グループをパーティションと呼ばれる論理的なセグメントに分割した構成
  - プレイスメントグループ内の各パーティションにそれぞれ一連のラックが有り、プレイスメントグループ内のパーティション同士が同じラックを共有しない。
  - ラックを分離することで、アプリケーション内のハードウェア障害の影響を隔離する。
- スプレッドプレースメントグループ
  - それぞれに独立のネットワーク及び電源が異なるラックに配置できるインスタンスグループ
  - 1AZ内のスプレッドプレイスメントグループに配置された7つのインスタンスは7つの異なるラックに配置される。
  - 少数の重要なインスタンスがお互いに分離して保持できる。同じラックを共有したときに発生する同時障害のリスクを軽減する。

#### AutoScaling

- 動的スケーリング
  - 簡易スケーリングポリシー
    - ターゲット追跡スケーリングポリシーの通常の設定。アラーム設定に基づいて1段階のスケーリングを実施
  - ステップスケーリングポリシー
    - アラームの超過サイズに基づいてインスタンス数を動的にスケーリングする。
- 手動スケーリング
  - 希望する容量を調整して手動でスケーリングを行う
- スケジュールされたスケーリング
  - スケジュールを実施する日時を指定してスケーリングを実行
  - スケーリングがうまく実行されずに24時間経った場合は自動的に処理が停止する。

#### Amazon Machine Image (AMI)

- 1 つまたは複数の EBS スナップショット、または、instance-store-backed AMI、インスタンスのルートボリュームのテンプレート
- 起動許可
- インスタンスの起動時にインスタンスにアタッチするボリュームを指定するブロックデバイスマッピング

### ELB

- EC2インスタンスの可用性を高めるためにELBを使用することができる。
- http/httpsではALBを使い、それ以外のTCPではNLBを使用する
- ELBには正常なインスタンスのみにトラフィックを送るためのヘルスチェック機能がある。
- ELBはインターネット向けにも内部向けにも対応している。
- インターネット向けだけではなく内部にもELBを挟むことによって、システムの可用性を高めることができる。
- ELB自体が高可用性のマネージドサービスなので、単一障害点とならない
- 複数のAZに負荷分散を実行できるのでリソース負荷が均等になる。

#### スティッキーセッション

- ELBがサーバにリクエスト振り分ける際、特定のCookieを確認することで、特定のクライアントからのリクエストを特定のサーバに紐付けることが出来る機能

### Auto Scaling

- Auto ScalingによってEC2インスタンスを必要な時に自動で増減できる
- Auto Scalingのメリットは高可用性、耐障害性、コスト効率化
- 垂直スケーリングよりも水平スケーリングのほうがスケーラビリティを確保しやすい
- Auto Scalingでは起動設定（何を）、AutoScalinグループ（どこで）、スケーリングポリシー（いつ）を設定する
- EC2のユーザーデータを使うことでコマンドを自動実行しデプロイ処理を自動化できる。
- EC2の情報はメタデータから取得できる。
- ELB、CloudWatch、Auto Scalingの3つのサービスで自動的でスケーラブルなアプリケーションを構築できる。

### Lambda

- サーバー構築や環境の準備をすることなくすぐに開発を始められる。
- サーバーの運用から解放され、開発に注力できる
- lambdaを使うために新しい言語の勉強は不要
- メモリを割り当てることでほかのリソースの性能も割り当てられる
- リクエストに応じて水平的にスケーリングして並行で関数が実行される。
- Auto Scalingを設定する必要がない
- 実行されている時間に対してミリ秒単位の無駄のない課金がされる
- 実行されていない待機時間には課金がない
- AWSサービスの処理を簡単に自動化できる
- AWSサービスからのトリガーを使用することで、イベントからlambdaを実行できる。

## AWSのストレージサービス

### ストレージの種類

1. ブロックストレージ
    - EC2にアタッチ
    - ブロック形式でデータを保存
    - 高速、高帯域幅
    - 例:EBS、インスタンスストア
2. オブジェクトストレージ
    - 例:S3,Glacier
    - オブジェクト形式でデータを保存
    - 安価かつ高耐久
3. ファイルストレージ
    - ファイル形式でデータを保存
    - 複数のEC2から同時にアタッチ可能
    - 例:EFS

### EFS

- EC2インスタンスからLAN上にあるNASとして利用できる共有ファイルストレージとして提供されています

#### マウントターゲット

- VPC 内の Amazon EFS ファイルシステムにアクセスするには、マウントターゲットが必要
- アベイラビリティーゾーンごとに 1 つのマウントターゲットを作成できる。
- VPC のアベイラビリティーゾーンに複数のサブネットがある場合、それらのサブネットの 1 つのみにマウントターゲットを作成できる。

### Storage Gateway

- オンプレアプリケーションとAWSのストレージをシームレスに接続。
- バックアップ、アーカイブ災害復旧、移行に使用

### EBS

- EBSはポイントインタイムスナップショットを作成することで、Amazon EBSボリュームのデータを Amazon S3 にバックアップして、データ消失を防ぐことができます。（増分バックアップ）
- 必要な時に必要な量を利用できる
- AZ内で自動的にレプリケートされる
- 使い始めた後で、ボリュームタイプを変更できる。
- 使い始めた後で、ストレージ容量を増加できる。
- スナップショットはS3の機能を使って保存される
- EBSの暗号化に対して、追加の操作は必要ない
- EBSのデータは永続的、インスタンスストアは一時的

#### EBSのRAID構成

- RAID0
  - パフォーマンス向上
  - 複数のディスクを1台のディスクのように扱う
  - ストライピング
- RAID1
  - ボリュームの冗長性の向上
  - RAID1では2つのボリュームを同時にミラーリングする

### S3

- オブジェクトタイプのストレージで、大量データを保存するのに向いている。
- ユーザー側で設定しなくても、AWS側でストレージリソースをスケールアップ/ダウンして、変動する需要に対応する。
- 複数のシステムにまたがる S3 オブジェクトをすべて自動的に作成して保存しており、99.999999999% (9 x 11) のデータ耐久性を実現するように設計。
- 世界中どこからでもアクセスできる。
- URL経由でアクセスが可能

#### S3の容量制限

- バケット
  - データ保存料歯無制限で自動でストレージが拡張される
- オブジェクト
  - バケット内に保存可能なオブジェクトは無制限
- 保存可能なオブジェクトサイズの制限
  - 0KB～5TBまで保存可能

#### S3の整合性モデル

昔は結果整合性モデルを利用していたが、現在は強い整合性モデルとなっており反映誤差が発生しない。

- 新規登録
  - 登録後即時にデータが反映
  - Consistency Read
- 更新
  - 強い整合性モデル
- 削除
  - 強い整合性モデル

#### S3のセキュリティ

- S3バケット、オブジェクトはデフォルトでプライベート
- ACLで簡単にアクセス権を制御
- バケットポリシーで詳細にアクセス権を設定可能
- ec2などのAWSリソースにS3のアクセス権を設定する際はIAMロールを使用する。
- HTTPSでアクセスできる
- 保存データの暗号化は複数の方法から選択できる。

#### S3の料金について

- ストレージ料金はストレージクラスによりコスト効率を高めることができる
- ライフサイクルポリシーによりストレージクラスの変更を自動化できる
- リージョン外へのアウト通信のみにデータ転送料金が発生する
- ストレージコストを比較すると最も値段が安いのがS3及びGlacier

- リージョン
  - リージョンごとに価格が異なる
- データ容量
  - データ量と保存期間に応じて時間がかかる
  - S3 Intelligent Tierring,IAストレージは30日分
- リクエストとデータ取得
  - データに対するリクエストに応じて料金がかかる
  - データを取得した量に応じて料金がかかる
- データ転送
  - データ転送イン；無料
  - インターネットへのデータ転送アウト(GB単位)
  - S3からAWS内でのデータ転送アウト(GB単位)

#### S3のタイプ

- STANDARD
  - 複数個所にデータを複製するため高耐久。
  - 頻繁に利用するデータの格納に向いている  
- STANDARD -IA
  - IA：Infrequent Access （低頻度アクセス）
  - 低頻度アクセスデータ用ストレージ
  - データの取得は早い
- ONEZONE-IA
  - 低頻度アクセスだがマルチAZ分散されていない
  - 重要ではないデータ向け。その分安い
- S3 Intelligent Tiering
  - 低頻度と高頻度の2つを持っている。ファイルは自動で低頻度に移動する。
  - 利用頻度がわからないデータ向け
- S3 Glacier Flexible Retrieval(通常のGlacier)
  - 1年数回のアクセス向け
  - データ検索で3~5時間
  - 迅速取り出しで2~5分で取り出し可能
  - 一括検索は5~12時間で無料でデータ取り出しが可能
  - ライフサイクル管理で利用指定できる
  - ボールトロック機能によりデータを保持・保護
- S3 Glacier Instant Retrieval
  - アクセスがほとんどなく、ミリ秒単位で取り出しが必要でデータ向け
  - S3 standardと同じパフォーマンスのデータ取り出し。
- Amazon Glacier DEEP Archive
  - 最安のストレージ
  - 7~10年以上保持される長時間使用されるもののアクセス頻度が低いデータ向け。
  - 標準取り出しは12時間以内
  - 大容量取り出しは48時間以内にデータを取得
  - ライフサイクル管理で利用指定できる

#### ライフサイクル管理

- バケット全体やPrefixに設定
- オブジェクト更新日を基準にして日単位で指定しｍ毎日0時(UTC)にキュー実行
- 最大1000ルール
- IAに移動できるのは128KB以上のオブジェクト
- MFA Deleteが友好だと設定不可

#### S3の特殊な機能

- Amazon S3 Transfer Acceleration
- 事前署名付き URL
- Cross-Origin Resource Sharing (CORS)
  - 特定のドメインにロードされたクライアントウェブアプリケーションが異なるドメイン内のリソースと通信する方法を定義する。
- S3 MFA Delete
  - バージョニング機能のオプション指定した削除操作のみMFA認証を要求する。
- オブジェクトロック
  - オブジェクトの削除・更新を一定時間ブロックする機能。Write Once Read Manyモデルを適用して最初のアップロード後は読み取りしか許可されない。
  - バージョンの保護
    - 保持期間
      - 一定期間のオブジェクトバージョンの上書きと削除を防ぐ
    - リーガルホールド
      - オブジェクトが削除サれるまでオブジェクトバージョンの上書きと削除を防ぐ
  - モード
    - ガバナンスモード
      - 特別なアクセス許可がないユーザーはオブジェクトのバージョンの上書きや削除ができない
    - コンプライアンスモード
      - ユートユーザー含めてすべてのユーザーがオブジェクトのバージョンの上書きや削除ができない

### S3のアクセス管理

- IAMユーザーポリシー
  - 内部のIAMユーザーやawsリソースへの権限管理
- バケットポリシー
  - 外部のユーザー含めたアクセス管理
- ACL
  - オブジェクトに個別に設定可能
- 事前署名付きURL
  - インターネット上の第三者にURLを閲覧させる。

### Amazon S3 Transfer Acceleration

- エッジロケーションを利用してクライアントと S3 バケットの間で、長距離にわたるファイル転送を高速、簡単、安全に行える

### マルチパートアップロード API

- 大容量オブジェクトをいくつかに分けてアップロードできる。



### Snowball

- 物理デバイスを利用して大容量のデータ転送ができる。
- エクサバイト級のデータ転送にはSnow mobileを使用する。

### AWS Snowball Edge

- AWSクラウドへの安全な大量データの転送を可能にするサービスです。
- セキュリティに考慮して設計されたデバイスを使用するペタバイト規模のデータ転送ソリューションで、AWS クラウド内外に大容量データを転送可能。

---

## ネットワークサービス

### VPC

### サブネット

## インターネットゲートウェイ

- VPC のインスタンスとインターネットとの間の通信を可能にする VPC コンポーネントです。VPCに設定することにより、インターネットとのアクセスを可能にする。

### インターネットゲートウェイの目的

1. インターネットでルーティング可能なトラフィックの送信先を VPC のルートテーブルに追加する。
2. パブリック IPv4 アドレスが割り当てられているインスタンスに対してネットワークアドレス変換 (NAT) を行う。

### ルートテーブル

### ネットワークACL

- 1 つ以上のサブネットのインバウンドトラフィックとアウトバウンドトラフィックを制御するファイアウォールとして動作する、VPC 用のセキュリティのオプションレイヤー

### 外部からEC2インスタンスにアクセスするには

### ハイブリッド構成環境

## カスタマーゲートウェイ

- VPC環境とオンプレ環境のつなぎこみをする時、接続の作業者側のアンカーです。(作業者側の回線の出口となります。)

## CloudFront

地域制限(地理的ブロッキング)を使用すると特定地域のアクセスを回避できる。

---

## データベースサービス

### RDS

- マルチAZで自動フェールオーバーを実現

### DynamoDB

## 管理サービス

### Cloudwatch

### Trusted Advisor

## 料金と請求

---



## AWS Database Migration Service （DMS）

## AWS Application Discovery Service

- オンプレミスデータセンターに関する情報を収集することにより、移行プロジェクト計画を支援しています。

## AWS CloudTrail

- ユーザーアクティビティログを取得することができる。
- ユーザー、ロール、または AWS のサービスによって実行されたアクションは、CloudTrail にイベントとして記録される。

## Amazon SNS

- マイクロサービス、分散型システム、およびサーバーレスアプリケーションの分離を可能にする、高可用性で耐久性に優れたセキュアな完全マネージド型 pub/sub メッセージングサービス。
- aws上でイベント通知、メッセージング処理、プッシュ通知をするときに用いる。

## Amazon SES

- デジタルマーケティング担当者やアプリケーション開発者がマーケティング、通知、トランザクションに関するEメールを送信できるように設計された、クラウドベースのEメール送信サービス

## Amazon SQS

- 完全マネージド型のメッセージキューイングサービスで、マイクロサービス、分散システム、およびサーバーレスアプリケーションの切り離しとスケーリングが可能です。プッシュ方式ではなくポーリング処理による通知を実施します。
- aws上でキューイング、タスク並列分散を使用するときに使用する。
- キュータイプ
  - 標準キュー
    - メッセージが少なくとも1回配信される
    - アプリケーションが1回以上順序が正確じゃなくても配信されればよいときに使用する。
  - FIFOキュー
    - FIFOで順番を守る
    - 操作順序、イベント順序が重要な場合に利用
- 可視性タイムアウト
  - 他のコンシューマが同じメッセージを受け取らないように設定する値
- ChangeMessageVisibility API
  - 可視性タイムアウトの時間を操作するAPI

## Amazon MQ

## Amazon RDS

- リードレプリカを追加することで可用性と耐久性を向上させることが可能であり、かつパフォーマンスも改善します。
- DB インスタンスの自動バックアップはデフォルトで Amazon S3 に取得される。
  
### RDSプロキシ

- アプリケーションとRDSデータベース間の仲介役として機能します。
- Lambda関数からデータベースに直接流れるすべてのデータベーストラフィックを処理します。

## Amazon Aurora

- DB インスタンスでは常に自動バックアップが有効になっています
- 標準のMySQLの最大5倍のスループットと、標準のPostgreSQLの最大3倍のスループットを実現
- マルチAZ分散のクラスター構成

## Amazon DynamoDB

- フルマネージド型の可用性の高いNoSQLサービス
- セッションデータの処理に向いており、高速で処理を実行できる。
- キャパシティモード
  - オンデマンドモード
    - キャパシティが予想できないときに使う
    - リクエストの実績に応じて課金
    - read/write処理に自動でスケーリング
  - プロビジョニングモード
    - キャパシティが事前にわかるときに使う
    - 事前にキャパシティユニットを設定する
    - キャパシティに応じた課金
    - キャパシティ容量に近づくとhttp400エラーが発せられる

### DynamoDBストリーム

- DynamoDBテーブルへの変更を監視できます。
- データの保存
  - 24時間以内の履歴を保存し、24時間経過で消去する。
  - データ容量はマネージドで自動的に管理
- データ保存の順番
  - 操作された順番に応じてシリアライズされる
  - 特定のハッシュキーに対する変更は正しい順番で保存される
  - ハッシュキーが異なる場合順番が前後する可能性がある

## Amazon Redshift

- 高速でシンプルかつ費用対効果の高いデータウェアハウスサービスです。
- 列指向データの分析に優れている
- 統計データを使用するので、常に最新の状態に保つ事が大事

### Amazon Redshift Spectrum

- Amazon S3に保存されているデータに対して直接SQLクエリを実行できる機能です。
- Amazon Redshift本体とは独立して処理が実行されるため、Redshiftに負荷をかけることなくデータ分析ができる。

## Amazon EMR

- オープンソースのフレームワークである Apache Spark と Hadoop を使用して、膨大な量のデータを迅速かつコスト効率よく処理して分析するサービス

## AWS Organizations

- アカウント作成を自動化して、ビジネスニーズを反映したアカウントのグループを作成し、それらのグループにポリシーを適用して管理できる。

## メモ

### 覚えておくべき移行関連のAWSサービス

1. AWS Application Discovery Service
    - サーバの使用データを提供し、移行に必要な情報を提供する。
2. AWS Database Migration Service
    - DBを短時間で安全にAWSに移行する
3. AWS Server Migration Service
    - オンプレミスワークロードを従来よりも簡単かつ短時間でAWSに移行する
4. AWS Schema Convertion TOOL
    - ソースデータベーススキーマ、ビュー、ストアドを自動的にターゲットデータベース互換フォーマットに変換する。

### 比較

1. Amazon SNS
    - AWS上のイベント通知やプッシュ通知
2. Amazon SES
    - Eメール
3. Amazon SQS
    - キューイング処理。ポーリング・PULL型の処理、並列分散処理

### AWSでセキュリティを向上させる

- 多要素認証（MFA）を設定して AWS リソースを保護することが推奨

### AWSの可用性について

- WSグローバルインフラストラクチャは主にリージョンとアベイラビリティーゾーン（AZ）によって構成されています。
- マルチAZ構成はAZを２つ利用した構成です。複数のAZを使用して同じリージョン内の複数のDC間でアプリケーションとデータをレプリケートすることにより、高い稼働率を達成することができる。
- マルチリージョン展開によって、ホットスタンバイやウォームスタンバイ構成をとることで、地震などの大きな災害でリージョンが停止するなどのリスクに対処できるようになる。
- インスタンスなどにオートスケーリングを実行することで、可用性を固めることは可能ですが、９９％以上のような高い稼働率を達成するのには不十分。

### ACLとセキュリティグループの違い

- ACL
  - VPC、サブネット単位で適用
  - 許可と拒否をin/outで指定
- セキュリティグループ
  - サーバー単位で適用
  - 許可のみをin/outで指定

### AWSのモニタリング系サービス

- Amazon Cloud Watch
  - ほとんどのAWSに自動適用。アラームなどを設定できる。
- AWS Cloud Trail
  - ユーザーアクティビティとAPI使用状況のログを取得し監視する
- AWS System Manager
  - AWSとオンプレ環境のモニタリングを統合管理し、運用タスクを自動化する。
  - パラメータストアを利用して資格情報を保存できる。しかし、ライフサイクル管理ができない
- AWS Config
  - AWSリソースの設定状況を評価し、AWSリソースの変更をモニタリングして履歴管理するサービス
- AWS Personal Hearth Dashboard
  - AWSサービスの異常正常ステータスをユーザーの利用状況に合わせて表示する。

### AWS SDK

### AWS プロフェッショナルサービス

- AWSでは利用者をサポートするため専門的なAWSプロフェッショナルサービスが提供されています。これはAWSクラウドを使用する際に望ましいビジネス成果を実現するのを支援できる専門家のグローバルチームです。

### Route53

- アプリケーションとWebサーバーおよびその他のリソースのヘルスとパフォーマンスを監視するヘルスチェックを提供します。

#### 位置情報ルーティング

- ユーザーの地理的場所に基づいてトラフィックを処理するリソースを選択できるルーティングポリシー
- このルーティングポリシーでコンテンツの配布を特定地域だけにできたりする。

### AWS OpsWorks

- Chef や Puppet のマネージド型インスタンスを利用した構成管理サービス

### AWS Elastic Beanstalk

- AWS クラウドのアプリケーションを迅速にデプロイし管理

### AWS CloudFormation

- テンプレートにAWSリソースを利用したインフラ構成をコードとして記述することで、1 つのスタックとして一括で起動し、設定できる。

### Elasticache

- ミリ秒未満のレイテンシを必要とするリアルタイムIoTアプリケーションのデータレイヤーに使用
- ダウンしたインスタンス以外にセッション情報を引き渡して継続して処理ができる

### コード関連のサービス

1. AWS CodeCommit
    - フルマネージド型のソース管理サービス
    - ソースコードからバイナリまでのあらゆるものを安全に保存でき、ライブラリなどのアプリケーション資産をコードとともに保存することが可能
2. AWS CodePipeline
    - パイプラインのリリースを自動化
3. AWS CodeBuild
    - クラウド内のコードをビルドおよびテストする。
4. AWS CodeDeploy
    - さまざまなコンピューティングサービスへのソフトウェアのデプロイを自動化

### Amazon Neptune

- フルマネージドグラフデータベースサービス
- データセットと連携するアプリケーションを簡単に構築および実行できる。

### AWS Security Token Service (AWS STS)

- AWS のサービスへのアクセスに使用できる一時的な限定権限認証情報を取得できる

### Amazon Cognito

- ウェブアプリケーションおよびモバイルアプリにユーザーのサインアップ/サインインおよびアクセスコントロールの機能を追加するサービス
- Amazon Cognitoの認証機能では、認証時のパスワード設定に加えて、多要素認証（MFA）を追加することが可能

### Amazon Elastic Container Registry (ECR)

- 完全マネージド型の Docker コンテナレジストリ

### Amazon Kinesis

- ストリームデータ処理に利用します。

#### Amazon Kinesis Data Streams

- ストリームデータ処理に利用するサービス(ミリ秒単位のリアルタイム処理)
- 集計するデータ処理を実装することができる
- Amazon Kinesis Data Firehoseよりも早い
- シャード単位で請求される

#### Amazon Kinesis Data Firehose

- ストリームデータ処理に利用するサービス(ただし60秒ごとにまとめて処理される)
- 集計するデータ処理を実装することができる
- ストリーム配信自体にはデータ保存不可
- Amazon Kinesis Data Streamsよりも設定が楽
- S3やRedshift,ElasticSearchにストリームデータを配信する。

#### Amazon Kinesis Data Analytics

- コンピュータやAmazon Kinesis Data Streams、Amazon Kinesis Data Firehoseから送信されてくるデータをSQLを使って処理できるサービス。

#### Kinesis クライアントライブラリ (KCL)

- KDSデータストリームからデータを処理できるカスタムコンシューマアプリケーションを構築できる。
- 分散コンピューティングに関連する複雑なタスクの多くを処理することで、Kinesis データストリームからデータを消費および処理するためのライブラリを提供します。

### Amazon API Gateway

- Amazon API Gateway は、あらゆる規模の REST、HTTP、および WebSocket API を作成、公開、維持、モニタリング、およびセキュア化するための AWS のサービス
- AWSまたは他のウェブサービス、AWSクラウドに保存されているデータにアクセスするAPIを作成できる。
- 使用料プランによりAPIキーにアクセス可能となるクォータ、アクセス頻度となるレート、バーストを設定できる。
- 使用料プランによりAPIの仕様回数を取得できる。
- APIキーを使用してAPIクライアントとユーザーを識別して、APIキーを持つ
- APIキーとLambdaオーソライザー、IAMロール、Amazon Cognitoを一緒に使用してAPIへのアクセスを制御できる。

### VPCエンドポイント

- VPCエンドポイントの種類
  - ゲートウェイ型エンドポイント
    - AWSサービスを宛先とするトラフィックのルートテーブルの宛先として指定できるゲートウェイ
    - DynamoDBとAmazonS3のみに適用可能
  - プライベートリンク型エンドポイント(インターフェース型)
    - プライベートIPアドレスを使用してサービスにプライベートにアクセスする。
    - AWS PrivateLinkはVPCとサービス間のすべてのネットワークトラフィックをAmazonネットワークに制限
    - RDS、EC2などの多くのAWSサービスに適用可能
    - AmazonS3に対応、DynamoDBは非対応

### AWS Certificate Manager

- 効率的な証明書通信の処理の管理が可能となる
- Amazon EventBridgeを利用することで、AWS Certificate Manager（ACM）のイベントをトリガーにしてアクションを実施することができる。(期限が切れる前に検知して通知等)

### AWS Nitro Enclaves

- 分離された仮想マシンで永続的なストレージを持たず、アクセス不可
- 暗号化証明
  - 許可されたコードのみが実行可
- リソースの柔軟な割当
  - EC2と同様に処理ができるようにCPU・メモリの組み合わせが多様

### S3のイベント通知

- S3のイベント通知は1つの機能しか受け取ることができない
- イベント通知をトリガに複数を並行して動かしたいときはSNSの通知を利用する。

### Amazon EventBridge

- イベントを使用してアプリケーションコンポーネントを接続するサーバーレスサービスです。
- スケーラブルなイベント駆動型アプリケーションを簡単に構築できる。
- アプリケーションの可用性の問題発生時やリソースの変更時などのシステムイベントに対するアクション処理などを実施できる。
- 簡単なルールを記述して、注目するイベントと、イベントがルールに一致した場合に自動的に実行するアクションを指定できる。
- 設定時にイベントソースとイベントタイプを選択できます。

### AWS Glue

- 抽出、変換、ロード (ETL) を行う完全マネージド型のサービスで分析用データの準備とロードを簡単にする。

#### AWS Glue データカタログ

- データの場所、スキーマ、およびランタイムメトリクスへのインデックス
- Data Catalog の情報はメタデータテーブルとして保存され、各テーブルが 1 つのデータストアを指定する
- Data Catalogに保持したデータに対してRedShiftで即座に解析処理を実行することが可能。

### AWS ParallelCluster

### AWS Secrets Manager

- 認証情報を安全に保存して、利用するための仕組みを提供している
- ライフサイクル管理機能を通じて、シークレットの管理、取得、ローテーションすることができる。

### Amazon Data Lifecycle Manager

- Amazon EBSのスナップショット取得のライフサイクルポリシーを設定できます

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIwMzAxMjU2MTgsNjA2NTQ3NDk5LC04Nj
MwNzkxODQsMTc5MjMyNzU0MiwtMTU2MjU5NjAzMSwtMTUwMjAz
NDU3NSwxOTUyMTMyMjA0LDgyMjUwMTU5NCwtMTY3MDIzNjc1OS
wyMTQyMzI0MDAzLC0yMzA3MjYyNjcsMjM5MjQ5MzMzLDMwNzU3
OTcxNywxNDU3MDMwMjQwLC05NTUwNjM4NzcsMjEwMDIwNDU2MC
wtMzcyMjk1ODkxLDIwMjk1MjAxODksNDY5NDg3MzAyLC01MTMx
OTA1MDldfQ==
-->