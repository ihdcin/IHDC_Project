from django.db import models

# Define the Transaction model first
class Transaction(models.Model):
    vendor = models.ForeignKey('Vendor', on_delete=models.CASCADE, related_name='transactions',default=None)
    description = models.TextField(null=True)
    amount = models.PositiveIntegerField()
    date = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return f'{self.vendor.vendor_name} - {self.amount} - {self.date.strftime("%Y-%m-%d")}'

# Define the Vendor model after the Transaction model
class Vendor(models.Model):
    vendor_name = models.CharField(max_length=30)
    account_number = models.BigIntegerField()
    ifsc_code = models.CharField(max_length=14)

    def __str__(self):
        return self.vendor_name
