import os
import django
import csv
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "getsuperfluid.settings")
django.setup()

from products.models import Product, ApplyOn, Category, ProductImage

CSV_PATH_PRODUCTS = "./products.csv"

with open(CSV_PATH_PRODUCTS) as in_file:
    data_reader = csv.reader(in_file)
    next(data_reader, None)
    for row in data_reader:
        #카테고리 입력
        if row[8]:
            category_name = row[8]
            Category.objects.create(name=category_name)
            
        #제품정보 입력
        product_name = row[0]
        description = row[1]
        super_tip = row[2]
        size = row[3]
        good_to_know = row[4]
        contains = row[5]
        price = row[6]
        category_id = Category.objects.filter(name=row[7])
        
        print(product_name,super_tip,size,price,category_id)

