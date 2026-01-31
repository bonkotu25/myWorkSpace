# SVF帳票生成フレームワーク

Spring BootアプリケーションでSVF(Super Visual Formador)を使った帳票PDF生成を簡単に実装するためのフレームワークです。

## 特徴

- ✅ **シンプルな実装**: DTOとMapperを作るだけでPDF生成が可能
- ✅ **型安全**: ジェネリクスによる型安全な設計
- ✅ **責務の分離**: データ(DTO)とマッピング処理(Mapper)を明確に分離
- ✅ **共通化**: エラーハンドリング、ログ出力などを共通サービスで一元管理
- ✅ **拡張性**: 新しい帳票追加時も既存コードへの影響なし

## アーキテクチャ

```
Controller
    ↓
  DTO作成
    ↓
ReportService.generatePdf(dto, mapper)
    ↓
Mapper.mapToReport(connection, dto)
    ↓
  SVF API
    ↓
PDF生成
```

## 必要な環境

- Java 11以上
- Spring Boot 2.x / 3.x
- SVF Java Edition
- Lombok (オプション)

## セットアップ

### 1. 依存関係の追加

```xml
<!-- pom.xml -->
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>

<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
    <optional>true</optional>
</dependency>

<!-- SVF Java Edition (バージョンは環境に応じて調整) -->
<dependency>
    <groupId>com.wingarc</groupId>
    <artifactId>svf-java-edition</artifactId>
    <version>X.X.X</version>
    <scope>system</scope>
    <systemPath>${project.basedir}/lib/svf.jar</systemPath>
</dependency>
```

### 2. 設定ファイル

```yaml
# application.yml
svf:
  template:
    path: /path/to/svf/templates
```

### 3. フレームワークコードの配置

以下のクラスをプロジェクトに追加します。実装例は`examples/`ディレクトリを参照してください。

## コア実装

### ディレクトリ構成

```
examples/
├── core/                           # フレームワークのコアクラス
│   ├── ReportMapper.java           # マッパーインターフェース
│   ├── ReportService.java          # 帳票生成サービス
│   ├── ReportGenerationException.java  # 例外クラス
│   └── PdfResponseHelper.java      # PDF応答ヘルパー
├── dto/                            # データ転送オブジェクト
│   └── InvoiceReportDto.java       # 請求書DTO例
├── mapper/                         # マッパー実装
│   └── InvoiceReportMapper.java    # 請求書マッパー例
└── controller/                     # コントローラー
    └── InvoiceController.java      # 請求書コントローラー例
```

## 使い方

### 1. DTOの作成

帳票に出力するデータを保持するクラスを作成します。

詳細は `examples/dto/InvoiceReportDto.java` を参照してください。

### 2. Mapperの作成

`ReportMapper<T>`を実装したMapperクラスを作成します。

詳細は `examples/mapper/InvoiceReportMapper.java` を参照してください。

### 3. Controllerでの使用

Controllerで`ReportService`を使ってPDFを生成します。

詳細は `examples/controller/InvoiceController.java` を参照してください。

## 実装チェックリスト

新しい帳票を追加する際のチェックリストです。

- [ ] DTOクラスを作成(データのみを保持)
- [ ] Mapperクラスを作成(`ReportMapper<T>`を実装)
- [ ] Mapperに`@Component`アノテーションを付与
- [ ] `getTemplateName()`でテンプレートファイル名を返す
- [ ] `mapToReport()`でDTOのデータをSVFにマッピング
- [ ] 繰り返し項目では必ず`writeLine()`を呼ぶ
- [ ] Controllerで`ReportService.generatePdf()`を呼び出す

## Tips & ベストプラクティス

### 日付フォーマット

```java
conn.setField("date", dto.getDate().format(
    DateTimeFormatter.ofPattern("yyyy/MM/dd")));
```

### 数値フォーマット

```java
DecimalFormat df = new DecimalFormat("#,###");
conn.setField("amount", df.format(dto.getAmount()));
```

### Null安全

```java
conn.setField("optionalField",
    dto.getOptionalValue() != null ? dto.getOptionalValue() : "");
```

### 繰り返し項目の注意点

```java
// ✅ 正しい実装
for (Item item : dto.getItems()) {
    conn.setField("itemName", item.getName());
    conn.writeLine();  // 必ず呼ぶ
}

// ❌ 間違った実装
for (Item item : dto.getItems()) {
    conn.setField("itemName", item.getName());
    // writeLine()がないと同じ行が上書きされる
}
```

## テスト例

### Mapperの単体テスト

```java
@ExtendWith(MockitoExtension.class)
class InvoiceReportMapperTest {

    @Mock
    private SVFConnection conn;

    @InjectMocks
    private InvoiceReportMapper mapper;

    @Test
    void テンプレート名が正しい() {
        assertThat(mapper.getTemplateName())
            .isEqualTo("invoice_template.svf");
    }

    @Test
    void DTOをSVFにマッピングできる() throws SVFException {
        // Given
        InvoiceReportDto dto = InvoiceReportDto.builder()
            .invoiceNumber("INV-001")
            .customerName("テスト株式会社")
            .build();

        // When
        mapper.mapToReport(conn, dto);

        // Then
        verify(conn).setField("invoiceNumber", "INV-001");
        verify(conn).setField("customerName", "テスト株式会社");
    }
}
```

## トラブルシューティング

### PDF生成エラーが発生する

1. ログを確認して詳細なエラーメッセージを確認
2. テンプレートファイルが正しい場所に配置されているか確認
3. SVFライセンスが有効か確認
4. フィールド名がテンプレートと一致しているか確認

### 文字化けが発生する

- SVFの文字コード設定を確認
- Javaの文字コード設定を確認(`-Dfile.encoding=UTF-8`)

### 同時実行でエラーが発生する

- SVFライセンスの同時実行数制限を確認
- 必要に応じてキューイング機構の導入を検討

## ライセンス

MIT License

## 作者

あずま よる
