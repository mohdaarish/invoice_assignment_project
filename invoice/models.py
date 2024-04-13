from django.db import models

# First Model For Invoice
class Invoice(models.Model):
    date = models.DateField()
    customer_care = models.CharField(max_length=100)


# Second Model For InvoiceDetails    
class InvoiceDetails(models.Model):
    Invoice = models.ForeignKey(Invoice, related_name="details", on_delete=models.CASCADE)
    descreption = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)