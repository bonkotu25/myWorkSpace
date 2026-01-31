package com.example.report;

import org.springframework.http.ContentDisposition;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Component;

import java.nio.charset.StandardCharsets;

/**
 * PDF応答生成のヘルパークラス
 */
@Component
public class PdfResponseHelper {

    /**
     * PDFをダウンロードさせるレスポンスを作成
     *
     * @param pdfBytes PDFのバイト配列
     * @param filename ダウンロードファイル名
     * @return ResponseEntity
     */
    public ResponseEntity<byte[]> createDownloadResponse(byte[] pdfBytes, String filename) {
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_PDF);
        headers.setContentDisposition(
            ContentDisposition.attachment()
                .filename(filename, StandardCharsets.UTF_8)
                .build()
        );

        return ResponseEntity.ok()
            .headers(headers)
            .body(pdfBytes);
    }

    /**
     * PDFをブラウザで表示するレスポンスを作成
     *
     * @param pdfBytes PDFのバイト配列
     * @return ResponseEntity
     */
    public ResponseEntity<byte[]> createInlineResponse(byte[] pdfBytes) {
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_PDF);
        headers.setContentDisposition(ContentDisposition.inline().build());

        return ResponseEntity.ok()
            .headers(headers)
            .body(pdfBytes);
    }
}
