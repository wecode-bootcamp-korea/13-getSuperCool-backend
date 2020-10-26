from django.db import models

class Product(models.Model):
    name            = models.CharField(max_length=45)
    description     = models.TextField(max_length=800)
    super_tip       = models.TextField(max_length=100,null=True)
    size            = models.CharField(max_length=20)
    good_to_know    = models.TextField(max_length=200)
    contains        = models.TextField(max_length=1000)
    price           = models.IntegerField()
    category        = models.ForeignKey('Category',on_delete=models.CASCADE)

    class Meta:
        db_table = 'products'

class ProductImage(models.Model):
    image_url       = models.URLField(max_length=1000)
    product         = models.ForeignKey('Product',on_delete=models.CASCADE)
    color           = models.ForeignKey('Color',on_delete=models.CASCADE,null=True)

    class Meta:
        db_table = 'product_images'

class Color(models.Model):
    name            = models.CharField(max_length=20)

    class Meta:
        db_table = 'colors'

class Category(models.Model):
    name            = models.CharField(max_length=10)

    class Meta:
        db_table = 'categories'

class ApplyOn(models.Model):
    name            = models.CharField(max_length=10)
    product         = models.ManyToManyField('Product',through='ProductApplyOn')

    class Meta:
        db_table = 'apply_ons'

class ProductApplyOn(models.Model):
    product         = models.ForeignKey('Product',on_delete=models.CASCADE)
    apply_on        = models.ForeignKey('ApplyOn',on_delete=models.CASCADE)

    class Meta:
        db_table = 'products_apply_ons'
