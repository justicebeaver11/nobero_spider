from djongo import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=255)
    price = models.CharField(max_length=50, null=True, blank=True)
    discount_percentage = models.CharField(max_length=50, null=True, blank=True)
    discount_flat = models.CharField(max_length=50, null=True, blank=True)
    mrp = models.CharField(max_length=50, null=True, blank=True)
    inclusive_taxes = models.CharField(max_length=50, null=True, blank=True)
    selected_color = models.CharField(max_length=255, null=True, blank=True)
    sizes = models.JSONField(null=True, blank=True)
    available_skus = models.JSONField(null=True, blank=True)
    fit = models.CharField(max_length=255, null=True, blank=True)
    fabric = models.CharField(max_length=255, null=True, blank=True)
    neck = models.CharField(max_length=255, null=True, blank=True)
    sleeve = models.CharField(max_length=255, null=True, blank=True)
    pattern = models.CharField(max_length=255, null=True, blank=True)
    length = models.CharField(max_length=255, null=True, blank=True)
    material = models.CharField(max_length=255, null=True, blank=True)
    origin = models.CharField(max_length=255, null=True, blank=True)
    wash_care = models.CharField(max_length=255, null=True, blank=True)
    please_note = models.CharField(max_length=255, null=True, blank=True)
    features = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.title
