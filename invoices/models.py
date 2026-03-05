from django.db import models
from decimal import Decimal

class Invoice(models.Model):
    invoice_number = models.PositiveIntegerField(unique=True, editable=False, null=True, blank=True)
    client_name = models.CharField(max_length=255)
    reference_no = models.CharField(max_length=100)
    date = models.DateField()
    subject = models.CharField(max_length=255)
    address = models.TextField(blank=True, null=True)
    mobile_number = models.CharField(max_length=20)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    work_description = models.TextField()
    office_company_name = models.CharField(max_length=255, blank=True, null=True)
    office_address = models.TextField(blank=True, null=True)
    office_phone_number = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_amount(self):
        return self.amount * self.quantity

    @property
    def vat_amount(self):
        return self.total_amount * Decimal("0.05")

    @property
    def grand_total(self):
        return self.total_amount + self.vat_amount

    def save(self, *args, **kwargs):
        if not self.invoice_number:
            # Get the last invoice number, or start from 9999 (so first one is 10000)
            last_invoice = Invoice.objects.filter(invoice_number__isnull=False).order_by('invoice_number').last()
            if last_invoice:
                self.invoice_number = last_invoice.invoice_number + 1
            else:
                self.invoice_number = 10000
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.reference_no} - {self.client_name}"

