from django.db import models

# Create your models here.


class Products(models.Model):
    GENDER = (
        ('M','M'), #male
        ('F','F'), #female
        ('U','U')  #unisex
    )

    id = models.AutoField(primary_key=True)
    product = models.CharField(max_length=100)
    purchase = models.CharField(max_length=10)
    sale = models.CharField(max_length=10)
    qty = models.CharField(max_length=10)
    gender = models.CharField(max_length=1, null=True, choices=GENDER)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product