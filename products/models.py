from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

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


#The parent class model
class Category(MPTTModel):
    name = models.CharField(max_length=255)
    parent = TreeForeignKey("self", on_delete= models.PROTECT, null = True, blank = True)   # Protect helps us to delete the child then the parent

    class MPTTMeta:
        order_insertion_by =['name']
        
    def __str__(self):
        return self.name


#the child class model
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_digital = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = TreeForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return (self.name + self.description)

    
class ProductLine(models.Model):
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock_qty = models.IntegerField()
    product = models.ManyToManyField(AttributValue)
    product_fk = models.ForeignKey(Product, on_delete=models.CASCADE)


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
