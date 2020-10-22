# Generated by Django 3.1.2 on 2020-10-22 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20201022_0731'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='review_date',
            new_name='created_at',
        ),
        migrations.AddField(
            model_name='review',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='comment',
            field=models.CharField(max_length=1000),
        ),
    ]