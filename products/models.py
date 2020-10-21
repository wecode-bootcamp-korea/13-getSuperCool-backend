from django.db import models

class Product(models.Model):
    name            = models.CharField(max_length=45)
    description     = models.TextField(max_length=800)
    super_tip       = models.TextField(max_length=100,null=True)
    size            = models.CharField(max_length=20)
    good_to_know    = models.TextField(max_length=200)
    contains        = models.TextField(max_length=1000)
    color           = models.CharField(max_length=20,null=True)
    price           = models.IntegerField()
    category1       = models.ForeignKey(Category1,on_delete=models.CASCADE)
   #review          = models.ForeignKey(reviews,on_delete=models.CASCADE)

    class Meta:
        db_table = 'products'

class ProductImage(models.Model):
    image_url       = models.URLField(max_length=1000)
    product         = models.ForeignKey(Product,on_delete=models.CASCADE)

    class Meta:
        db_table = 'product_images'

class Category1(models.Model):
    name            = models.CharField(max_length=10)

    class Meta:
        db_table = 'category1'

class Category2(models.Model):
    name            = models.CharField(max_length=10)
    product         = models.ManyTomanyField(Product)

    class Meta:
        db_table = 'category2'

