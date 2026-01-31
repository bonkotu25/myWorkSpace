package com.example.dto;

import lombok.Builder;
import lombok.Data;

import java.math.BigDecimal;
import java.time.LocalDate;
import java.util.List;

/**
 * 請求書帳票用DTO
 */
@Data
@Builder
public class InvoiceReportDto {
    private String invoiceNumber;
    private LocalDate invoiceDate;
    private String customerName;
    private String customerAddress;
    private List<InvoiceItemDto> items;
    private BigDecimal totalAmount;
    private BigDecimal taxAmount;
}
