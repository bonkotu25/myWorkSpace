# AI技術要素メモ

## 11/06

### はじめに

- 気軽に聞いてね。
- わからないことや知りたいことは情報もらえると私も調べます。

### 話したいこと

- そもそものLLMの話
  - どんな種類があるの？
    - Gemini
    - gpt
    - calude
  - どんな特徴があるの？
    - Gemini
      - google関連サービスとの連携が強い
      - コンテキスト長が圧倒的に長い
    - gpt(codex)
      - 図解が優秀
      - 音声、画像、動画を処理できる。
    - calude(claude code)
      - 設計・実装とかの分野に強い
      - 日本語に強く、長文のライティングに向いている

- AIコーディングツールセクション
  - リアルタイム補完型
    - GitHub Copilot
      - エディタ内でリアルタイムにコード補完
      - 関数名やコメントから実装を予測
      - 最も広く使われている
  - エディタ統合型
    - Cursor
      - VS Codeフォーク
      - コードベース全体を理解した提案
    - Windsurf
      - 同様にVS Codeベース
      - 複数ファイルの編集に対応
  - 仕様駆動開発型
    - Kiro
      - Spec駆動開発 →仕様を固めてから周辺のドキュメントを作っていく
        - requirements.md（要件定義）
        - design.md（設計）
        - tasks.md（タスクリスト）
          を自動生成してから実装  
      - VS Codeベース、Claude Sonnet搭載
    - cc-sdd（国産オープンソース）[記事](https://zenn.dev/canly/articles/c77bf9f7a67582)・[記事その2](https://zenn.dev/kokushing/articles/7468d5f195e54c)
      - Kiroと同じ思想だが、より柔軟
        - 同じくrequirements.md、design.md、tasks.mdを生成
        - 各フェーズで人間の承認が必要（AI任せにしない）
      - 対応ツール： Claude Code、Cursor、Gemini CLI
      - 既存のエディタをそのまま使える
      - 導入が簡単： `npx cc-sdd@latest --lang ja` の1コマンド
      - 日本語完全対応（ドキュメントも日本語）
    - **比較：**
      - Kiro：専用エディタ、ウェイトリスト必要
      - cc-sdd：好きなエディタで使える、すぐ試せる、日本語対応
  - ターミナル型
    - Claude Code
      - ターミナルから操作
      - 複数ファイルの自律的な編集
      - プロジェクト全体の把握に強い
  - チャット型
    - ChatGPT/Claude/Gemini
      - コンサル的な使い方
      - 設計相談、コードレビュー
      - アーキテクチャ検討

---

- cursor2.0の話
  - [記事](https://zenn.dev/aimasaou/articles/5553db1e139907)
  - Composer
    - コーディング特化
    - 処理速度が早い(Haiku 4.5、Gemini Flash 2.5より早い)
    - 考える力は強くない(GPT-5やClaude Sonnet 4.5には及ばない)
    - 使い方は？
      - 設計までできたプロンプトを渡して実装させる用途が強い(きがする)