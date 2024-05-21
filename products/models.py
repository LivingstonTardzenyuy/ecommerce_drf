from django.db import models


# Create your models here.
class Attribute(models.Model):
    name = models.CharField(max_length=255)


class AttributValue(models.Model):
    value = models.CharField(max_length=255)
    attribute = models.ForeignKey(
        Attribute, on_delete=models.CASCADE, related_name="attribute"
    )


class Brand(models.Model):
    name = models.CharField(max_length=255)


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_digital = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)


class ProductLine(models.Model):
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock_qty = models.IntegerField()
    product = models.ManyToManyField(AttributValue)
    product_fk = models.ForeignKey(Product, on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=255)
    product = models.ManyToManyField(Product)


class ProductImage(models.Model):
    name = models.CharField(max_length=255)
    alternative_text = models.CharField(max_length=255)
    url = models.ImageField(
        blank=True,
        null=True,
        upload_to="productImage/",
        verbose_name="My Image Field",
        validators=[],
        help_text="This is an image field.",
    )
    product_line = models.ForeignKey(ProductLine, on_delete=models.CASCADE)
