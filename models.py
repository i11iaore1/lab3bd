from django.db import models
# Create your models here.

class Shop(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    age = models.IntegerField(null=True)

    class Meta:
        db_table = 'shop'


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    shopid = models.ForeignKey(Shop, on_delete=models.CASCADE, db_column="shopid")
    surname = models.CharField(max_length=20)
    age = models.IntegerField()
    phone = models.CharField(unique=True, max_length=13)

    class Meta:
        db_table = 'employee'


class Storebranch(models.Model):
    id = models.AutoField(primary_key=True)
    shopid = models.ForeignKey(Shop, on_delete=models.CASCADE, db_column="shopid")
    name = models.CharField(max_length=30)

    class Meta:
        db_table = 'storebranch'


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=20)
    storebranchid = models.ForeignKey(Storebranch, on_delete=models.CASCADE, db_column="storebranchid")
    sellprice = models.IntegerField()
    sold = models.BooleanField(null=True)

    class Meta:
        db_table = 'product'


class Orders(models.Model):
    id = models.AutoField(primary_key=True)
    shopid = models.ForeignKey(Shop, on_delete=models.CASCADE, db_column="shopid")
    price = models.IntegerField()


class Product_orders(models.Model):
    ordersid = models.ForeignKey(Orders, primary_key=True, on_delete=models.CASCADE, unique=False, db_column="ordersid")
    productid = models.ForeignKey(Product, on_delete=models.CASCADE, unique=False, db_column="productid")

    class Meta:
        unique_together = (('ordersid', 'productid'),)
        db_table = 'product_orders'