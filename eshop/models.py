from django.db import models
from django.contrib.auth.models import User

class Manufacturer(models.Model):
    name = models.CharField(max_length=80)
    
    def __unicode__(self):
        return self.name

class Currency(models.Model):
    # Name, for example "British pound"
    name = models.CharField(max_length=20)
    
    # Symbol, for example "EUR"
    symbol = models.CharField(max_length=3)
    
    def __unicode__(self):
        return self.name + ' (' + self.symbol + ')'

class Product(models.Model):
    # Title for the product, tells the customer what the product is
    title = models.CharField(max_length=80)

    # When a product is modified, a new Product is created and the old
    # one is deactivated. Older products are not removed or modified,
    # since they may be referenced in an order
    active = models.BooleanField(default=True)
      
    # Manufacturer of the product
    manufacturer = models.ForeignKey(Manufacturer, null=True, blank=True)

    # A one sentence description of the product
    short_description = models.CharField(max_length=100)
    
    # A full description to be shown in select views
    long_description = models.TextField(blank=True)
    
    # Price, up to 9999 units, two decimal places
    price = models.DecimalField(max_digits=4, decimal_places=2)
    
    # Currency of the price
    currency = models.ForeignKey(Currency)

    # A picture of the product
    #image = models.ImageField(null=True, upload_to='images')
    # See http://docs.djangoproject.com/en/dev/ref/models/fields/#imagefield

    def __unicode__(self):
        return self.title + ' (price ' + str(self.price) +\
            ' ' + self.currency.symbol + ')'

class Category(models.Model):
    """Product categories"""
    # A title for the category, shown on the category list
    title = models.CharField(max_length=80)
    
    # A description is shown in selected views, maybe floats, etc.
    description = models.CharField(max_length=100)

    # If there is a hierarchy for categories, define parent for this category
    parent = models.ForeignKey('Category', null=True)

class Cart(models.Model):
    """The shopping cart which contains the products the user has chosen"""
    
    # The owner
    customer = models.ForeignKey(User)

    # The products in the cart
    products = models.ManyToManyField(Product)

class Order(models.Model):
    """An order entity is created when the customer has paid the order"""

    # Who bought it?
    customer = models.ForeignKey(User)
    
    # Address where to send the product
    streetaddress = models.CharField(max_length=80)
    zip = models.CharField(max_length=5)
    city = models.CharField(max_length=40)

    # Total price of the products
    totalprice = models.DecimalField(max_digits=4, decimal_places=2)

    # The products ordered
    products = models.ManyToManyField(Product)

    # Status of the order
    STATUS_CHOICES=(
                    ('waiting', 'Waiting'),
                    ('sent', 'Sent to customer'),
                    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    