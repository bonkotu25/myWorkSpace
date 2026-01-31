package com.example.report;

/**
 * SVF帳票マッピング用インターフェース
 * 新しい帳票を追加する場合、このインターフェースを実装したMapperを作成する
 *
 * @param <T> 対応するDTOの型
 */
public interface ReportMapper<T> {

    /**
     * 使用するSVFテンプレートファイル名を返す
     *
     * @return テンプレートファイル名 (例: "invoice_template.svf")
     */
    String getTemplateName();

    /**
     * DTOのデータをSVFにマッピングする
     *
     * @param conn SVF接続オブジェクト
     * @param dto マッピング元のDTO
     * @throws SVFException SVF処理でエラーが発生した場合
     */
    void mapToReport(SVFConnection conn, T dto) throws SVFException;

    /**
     * 生成されるPDFのファイル名を返す
     * デフォルト実装ではテンプレート名から.svfを.pdfに置換
     *
     * @param dto DTO
     * @return ファイル名
     */
    default String getFileName(T dto) {
        return getTemplateName().replace(".svf", ".pdf");
    }
}
