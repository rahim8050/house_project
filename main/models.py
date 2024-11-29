from django.db import models

# Create your models here.
class House(models.Model):
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    plot_no =models.CharField(max_length=30)
    house_no = models.CharField(max_length=30, unique=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']
        db_table = 'houses'


class House_info(models.Model):
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    door_no = models.CharField(max_length=30, unique=True)
    year = models.IntegerField()
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'House_info'
        verbose_name_plural = 'House_infos'
        db_table = 'house_infos'
        ordering = ['door_no']

class Renting(models.Model):
    house = models.ForeignKey(House_info, on_delete=models.CASCADE)
    name = models.ForeignKey(House, on_delete=models.CASCADE, related_name='borrower')
    status = models.CharField(max_length=30)
    expected_rent_date = models.DateField()
    rent_date = models.DateField(null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.name

    @property
    def fine_total(self):
        if self.rent_date and self.expected_rent_date and self.rent_date > self.expected_rent_date:
            amount = (self.rent_date - self.expected_rent_date).days * 13
            return amount
        return 0
    class Meta:
        verbose_name = 'Renting'
        verbose_name_plural = 'Rentings'
        db_table = 'renting'
        ordering = ['-created_at']

class Payment(models.Model):
    renting = models.ForeignKey(Renting, on_delete=models.CASCADE)
    merchant_request_id = models.CharField(max_length=100)
    checkout_request_id = models.CharField(max_length=120)
    code = models.CharField(max_length=50, null=True, blank=True)
    amount = models.IntegerField(default=0)
    status = models.CharField(max_length=50, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.code
    class Meta:
            verbose_name = 'payment'
            verbose_name_plural = 'payments'
            db_table = 'payments'
            ordering = ['-created_at']







