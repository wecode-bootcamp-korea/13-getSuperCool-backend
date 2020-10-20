from django.db import models

class Product(models.Model):
    name            = models.CharField(max_length=45)
    description     = models.TextField(max_length=1000)
    price           = models.IntegerField()
    ingredients     = models.TextField(max_length=1000)
    color           = models.CharField(max_length=45, null=True)
    category1       = models.ForeignKey(Category1, on_delete=models.CASCADE)

    class Meta:
        db_table = 'products'


class Category1(models.Model):
    name            = models.CharField(max_length=10)

    class Meta:
        db_table = 'category1'


class Category2(models.Model):
    name            = models.CharField(max_length=10)
    product         = models.ManyTomanyField(Product)

    class Meta:
        db_table = 'category2'

