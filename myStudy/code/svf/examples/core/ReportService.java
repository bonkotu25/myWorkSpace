package com.example.report;

import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

/**
 * SVF帳票生成の共通サービス
 * 全ての帳票生成はこのサービスを経由する
 */
@Slf4j
@Service
public class ReportService {

    @Value("${svf.template.path}")
    private String templatePath;

    /**
     * DTOとMapperを使ってPDFを生成する
     *
     * @param dto 帳票データDTO
     * @param mapper DTOをSVFにマッピングするMapper
     * @param <T> DTOの型
     * @return 生成されたPDFのバイト配列
     * @throws ReportGenerationException PDF生成に失敗した場合
     */
    public <T> byte[] generatePdf(T dto, ReportMapper<T> mapper) {

        validateInputs(dto, mapper);

        try (SVFConnection conn = createConnection()) {
            conn.connect();

            // テンプレート読み込み
            String templateName = mapper.getTemplateName();
            conn.openReport(templatePath + "/" + templateName);

            // Mapperでデータマッピング
            mapper.mapToReport(conn, dto);

            // PDF生成
            byte[] pdfBytes = conn.generatePdf();

            logSuccess(mapper, dto);
            return pdfBytes;

        } catch (SVFException e) {
            logError(mapper, dto, e);
            throw new ReportGenerationException(
                "帳票生成に失敗しました: " + mapper.getTemplateName(), e);
        }
    }

    /**
     * PDFファイル名を取得する
     *
     * @param dto DTO
     * @param mapper Mapper
     * @param <T> DTOの型
     * @return ファイル名
     */
    public <T> String getFileName(T dto, ReportMapper<T> mapper) {
        return mapper.getFileName(dto);
    }

    private <T> void validateInputs(T dto, ReportMapper<T> mapper) {
        if (dto == null) {
            throw new IllegalArgumentException("DTOがnullです");
        }
        if (mapper == null) {
            throw new IllegalArgumentException("Mapperがnullです");
        }
        if (mapper.getTemplateName() == null || mapper.getTemplateName().isEmpty()) {
            throw new IllegalArgumentException("テンプレート名が未設定です");
        }
    }

    private SVFConnection createConnection() {
        // SVF接続の初期化処理
        // ライセンス設定などもここで実施
        return new SVFConnection();
    }

    private <T> void logSuccess(ReportMapper<T> mapper, T dto) {
        log.info("帳票生成成功: template={}, dto={}",
            mapper.getTemplateName(), dto.getClass().getSimpleName());
    }

    private <T> void logError(ReportMapper<T> mapper, T dto, Exception e) {
        log.error("帳票生成失敗: template={}, dto={}, error={}",
            mapper.getTemplateName(), dto.getClass().getSimpleName(), e.getMessage(), e);
    }
}
