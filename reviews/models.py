from django.db      import models

class Review(models.Model):
    user       = models.ForeignKey('users.User',on_delete=models.CASCADE)
    caption    = models.CharField(max_length=45)
    user_name  = models.CharField(max_length=10)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    comment    = models.CharField(max_length=1000)
    score      = models.ForeignKey('Score',on_delete=models.CASCADE)
    age_range  = models.ForeignKey('AgeRange',on_delete=models.CASCADE,null=True)
    skin_shade = models.ForeignKey('SkinShade',on_delete=models.CASCADE,null=True)
    skin_type  = models.ForeignKey('SkinType',on_delete=models.CASCADE,null=True)
    product    = models.ForeignKey('products.Product',on_delete=models.CASCADE)

    class Meta:
        db_table = 'reviews'

class Score(models.Model):
    score = models.IntegerField()

    class Meta:
        db_table = 'scores'

class AgeRange(models.Model):
    age_range = models.CharField(max_length=10)

    class Meta:
        db_table = 'age_ranges'

class SkinShade(models.Model):
    skin_shade = models.CharField(max_length=10)

    class Meta:
        db_table = 'skin_shades'

class SkinType(models.Model):
    skin_type = models.CharField(max_length=10)

    class Meta:
        db_table = 'skin_types'

class ReviewImage(models.Model):
    image_url = models.URLField(max_length=1000)
    review    = models.ForeignKey('Review',on_delete=models.CASCADE)

    class Meta:
        db_table = 'review_images'


