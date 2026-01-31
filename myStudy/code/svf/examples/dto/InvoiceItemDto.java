package com.example.dto;

import lombok.Data;

import java.math.BigDecimal;

/**
 * 請求書明細項目DTO
 */
@Data
public class InvoiceItemDto {
    private String itemName;
    private Integer quantity;
    private BigDecimal unitPrice;
    private BigDecimal amount;
}
