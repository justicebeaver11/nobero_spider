import scrapy
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nobero_project.settings')
django.setup()

class NoberoSpider(scrapy.Spider):
    name = 'nobero_spider'
    start_urls = [
        'https://nobero.com/pages/men',
        'https://nobero.com/products/lunar-echo-oversized-t-shirt-1?variant=45663963218086'
    ]

    def parse(self, response):
        if "pages/men" in response.url:
            # Call the method to parse the category page
            return self.parse_category_page(response)
        else:
            # Call the method to parse the product page
            return self.parse_product_page(response)

    def parse_category_page(self, response):
        # Extract the category name and URL
        category_name = response.css('#product-info h3::text').get().strip()
        category_url = response.css('a.product_link::attr(href)').get()

        # Yield the category details
        yield {
            'category_name': category_name,
            'category_url': category_url
        }

        # If you want to pass this information to the product page parser
        for url in self.start_urls:
            if "products" in url:
                yield scrapy.Request(url, callback=self.parse_product_page, meta={'category_name': category_name, 'category_url': category_url})

    def parse_product_page(self, response):
        # Get category name and URL from meta if needed
        category_name = response.meta.get('category_name')
        category_url = response.meta.get('category_url')

        # Extract product details
        title = response.css('h1.capitalize.text-lg.md\\:text-\\[1\\.375rem\\].font-\\[familySemiBold\\].leading-none::text').get().strip()
        price = response.css('#price-template--16047755657382__main').css('h2#variant-price::text').get()
        discount_percentage = response.css('#price-template--16047755657382__main').css('h2#variant-save-percentage::text').get()
        discount_flat = response.css('#price-template--16047755657382__main').css('h2#variant-save-flat::text').get()
        mrp = response.css('#price-template--16047755657382__main').css('h2 span#variant-compare-at-price::text').get()
        inclusive_taxes = response.css('#price-template--16047755657382__main').css('div span.font-[familyRegular]::text').get()

        available_skus = []
        sku_elements = response.css('YOUR_SKU_CONTAINER_SELECTOR')
        for sku in sku_elements:
            color = sku.css('YOUR_COLOR_SELECTOR::text').get().strip()
            sizes = sku.css('YOUR_SIZE_SELECTOR::text').getall()
            available_skus.append({
                'color': color,
                'size': sizes
            })

        color = response.css('fieldset.product-form-input label.relative.cursor-pointer.color-select input::attr(value)').getall()
        selected_color = response.css('#selected-color-title::text').get().strip()
        sizes = response.css('fieldset.grid.w-full.grid-template-columns-autofill label.relative.cursor-pointer.size-select input::attr(value)').getall()
        fit = response.css('div.product-metafields-values:nth-of-type(1) p::text').get()
        fabric = response.css('div.product-metafields-values:nth-of-type(2) p::text').get()
        neck = response.css('div.product-metafields-values:nth-of-type(3) p::text').get()
        sleeve = response.css('div.product-metafields-values:nth-of-type(4) p::text').get()
        pattern = response.css('div.product-metafields-values:nth-of-type(5) p::text').get()
        length = response.css('div.product-metafields-values:nth-of-type(6) p::text').get()
        material = response.css('p > strong:contains("Material:") + span::text').get()
        neck = response.css('p > strong:contains("Neck:") + span::text').get()
        sleeves = response.css('p > strong:contains("Sleeves:") + span::text').get()
        origin = response.css('p > strong:contains("Origin:") + span::text').get()
        wash_care = response.css('p > strong:contains("Wash Care:") + span::text').get()
        please_note = response.css('p > strong:contains("Please Note:") + span::text').get()

        features = response.css('p > strong:contains("Features:") + span + br + span::text').getall()
        features = [f.strip() for f in features if f.strip()]

        extra_features = response.css('p > strong:contains("Features:") ~ span::text').getall()
        extra_features = [ef.strip() for ef in extra_features if ef.strip()]

        all_features = features + extra_features

        # Yield the product details along with the category info
        yield {
            'title': title,
            'price': price,
            'discount_percentage': discount_percentage,
            'discount_flat': discount_flat,
            'mrp': mrp,
            'inclusive_taxes': inclusive_taxes,
            'color': color,
            'selected colors': selected_color,
            'sizes': sizes,
            'available_skus': available_skus,
            'fit': fit,
            'fabric': fabric,
            'neck': neck,
            'sleeve': sleeve,
            'pattern': pattern,
            'length': length,
            'material': material,
            'neck': neck,
            'sleeves': sleeves,
            'features': all_features,
            'origin': origin,
            'wash_care': wash_care,
            'please_note': please_note,
            'category_name': category_name,
            'category_url': category_url,
        }
   
from products.models import Category, Product
    