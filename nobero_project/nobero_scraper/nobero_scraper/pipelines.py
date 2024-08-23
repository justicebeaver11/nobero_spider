# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter


# class NoberoScraperPipeline:
#     def process_item(self, item, spider):
#         return item
# scrapy_project/pipelines.py
from products.models import Product

class MongoDBPipeline(object):
    def process_item(self, item, spider):
        # Map Scrapy item to Django model fields
        product = Product(
            title=item.get('title'),
            price=item.get('price'),
            discount_percentage=item.get('discount_percentage'),
            discount_flat=item.get('discount_flat'),
            mrp=item.get('mrp'),
            inclusive_taxes=item.get('inclusive_taxes'),
            color=item.get('color'),
            selected_colors=item.get('selected_colors'),
            sizes=item.get('sizes'),
            available_skus=item.get('available_skus'),
            fit=item.get('fit'),
            fabric=item.get('fabric'),
            neck=item.get('neck'),
            sleeve=item.get('sleeve'),
            pattern=item.get('pattern'),
            length=item.get('length'),
            material=item.get('material'),
            sleeves=item.get('sleeves'),
            features=item.get('features'),
            origin=item.get('origin'),
            wash_care=item.get('wash_care'),
            please_note=item.get('please_note'),
        )
        product.save()
        return item
