package com.example.mapper;

import com.example.dto.InvoiceReportDto;
import com.example.dto.InvoiceItemDto;
import com.example.report.ReportMapper;
import org.springframework.stereotype.Component;

/**
 * 請求書帳票マッパー
 */
@Component
public class InvoiceReportMapper implements ReportMapper<InvoiceReportDto> {

    @Override
    public String getTemplateName() {
        return "invoice_template.svf";
    }

    @Override
    public void mapToReport(SVFConnection conn, InvoiceReportDto dto)
        throws SVFException {

        // ヘッダー項目のマッピング
        conn.setField("invoiceNumber", dto.getInvoiceNumber());
        conn.setField("invoiceDate", dto.getInvoiceDate().toString());
        conn.setField("customerName", dto.getCustomerName());
        conn.setField("customerAddress", dto.getCustomerAddress());
        conn.setField("totalAmount", dto.getTotalAmount().toString());
        conn.setField("taxAmount", dto.getTaxAmount().toString());

        // 明細行のマッピング(繰り返し項目)
        for (InvoiceItemDto item : dto.getItems()) {
            conn.setField("itemName", item.getItemName());
            conn.setField("quantity", item.getQuantity().toString());
            conn.setField("unitPrice", item.getUnitPrice().toString());
            conn.setField("amount", item.getAmount().toString());
            conn.writeLine();  // 1行書き出し
        }
    }

    @Override
    public String getFileName(InvoiceReportDto dto) {
        return "invoice_" + dto.getInvoiceNumber() + ".pdf";
    }
}
