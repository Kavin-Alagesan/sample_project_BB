from django.db import models

# Create your models here.

class Customer(models.Model):
    customer_id=models.AutoField(primary_key=True)
    customer_name=models.CharField(max_length=100)

    def __str__(self):
        return self.customer_name

class Tags(models.Model):
    tags_id=models.AutoField(primary_key=True)
    tag_name=models.CharField(max_length=100)

    def __str__(self):
        return self.tag_name

class Product(models.Model):
    product_id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=250)
    tags=models.ManyToManyField(Tags)

    def __str__(self):
        return self.product_name

class Orders(models.Model):
    STATUS=(
        ('PENDING','PENDING'),
        ('OUT FOR DELIVERY','OUT FOR DELIVERY'),
        ('DELIVERED','DELIVERED'),
    )
    order_id=models.AutoField(primary_key=True)
    customer_id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    product_id=models.ForeignKey(Product,on_delete=models.CASCADE)
    order_status=models.CharField(max_length=50,null=True,choices=STATUS)

    def __str__(self):
        return self.order_status
