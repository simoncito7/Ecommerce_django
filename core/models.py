from django.db import models
from django.conf import settings
from django.shortcuts import reverse


class Item(models.Model):

    CATEGORY_CHOICES = (
        ('S', 'Shirt'),
        ('SW', 'Sport Wear'),
        ('OW', 'Outwear'),
    )

    LABEL_CHOICES = (
        ('P', 'primary'),
        ('S', 'secondary'),
        ('D', 'danger'),
    )

    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(
        max_length=2, choices=CATEGORY_CHOICES, default='S')

    label = models.CharField(choices=LABEL_CHOICES, max_length=2, default='P')
    # A "slug" is a way of generating a valid URL, generally using data already obtained. For instance, a slug uses the title of an article to generate a URL
    slug = models.SlugField(default=" ")
    description = models.TextField(default=" ")

    def __str__(self):
        return self.title
    # method to manage the urls linked to a specific product

    def get_absolute_url(self):
        return reverse('core:product', kwargs={'slug': self.slug})

    def get_add_to_cart_url(self):
        return reverse('core:add-to-cart', kwargs={'slug': self.slug})


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    # to keep track of how many orders we have
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
