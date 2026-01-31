package com.example.controller;

import com.example.dto.InvoiceReportDto;
import com.example.dto.InvoiceItemDto;
import com.example.mapper.InvoiceReportMapper;
import com.example.report.PdfResponseHelper;
import com.example.report.ReportService;
import com.example.service.InvoiceService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.stream.Collectors;

/**
 * 請求書コントローラー
 */
@RestController
@RequestMapping("/api/invoices")
@RequiredArgsConstructor
public class InvoiceController {

    private final InvoiceService invoiceService;
    private final ReportService reportService;
    private final InvoiceReportMapper invoiceMapper;
    private final PdfResponseHelper pdfHelper;

    @GetMapping("/{invoiceId}/pdf")
    public ResponseEntity<byte[]> downloadPdf(@PathVariable Long invoiceId) {

        // 1. データ取得
        Invoice invoice = invoiceService.findById(invoiceId);

        // 2. DTO変換
        InvoiceReportDto dto = InvoiceReportDto.builder()
            .invoiceNumber(invoice.getInvoiceNumber())
            .invoiceDate(invoice.getInvoiceDate())
            .customerName(invoice.getCustomerName())
            .customerAddress(invoice.getCustomerAddress())
            .items(convertToItemDtos(invoice.getItems()))
            .totalAmount(invoice.getTotalAmount())
            .taxAmount(invoice.getTaxAmount())
            .build();

        // 3. PDF生成
        byte[] pdf = reportService.generatePdf(dto, invoiceMapper);

        // 4. レスポンス返却
        String filename = reportService.getFileName(dto, invoiceMapper);
        return pdfHelper.createDownloadResponse(pdf, filename);
    }

    private List<InvoiceItemDto> convertToItemDtos(List<InvoiceItem> items) {
        return items.stream()
            .map(item -> {
                InvoiceItemDto dto = new InvoiceItemDto();
                dto.setItemName(item.getItemName());
                dto.setQuantity(item.getQuantity());
                dto.setUnitPrice(item.getUnitPrice());
                dto.setAmount(item.getAmount());
                return dto;
            })
            .collect(Collectors.toList());
    }
}
