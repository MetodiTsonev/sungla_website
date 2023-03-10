from django.conf import settings
from django.db import models
from django.urls import reverse


class Item(models.Model):
    C_CHOICES = {
        ('Glasses', 'Glasses')
    }

    image = models.ImageField(upload_to=settings.MEDIA_ROOT)
    title = models.CharField(max_length=30)
    price = models.FloatField()
    category = models.CharField(choices=C_CHOICES, max_length=7)
    slug = models.SlugField()
    description = models.TextField(default='Try Them On!')

    def get_absolute_url(self):
        return reverse('product', kwargs={
            'slug': self.slug,
        })

    def get_add_to_cart_url(self):
        return reverse('add to cart', kwargs={
            'slug': self.slug,
        })

    def get_remove_from_cart_url(self):
        return reverse('remove from cart', kwargs={
            'slug': self.slug,
        })


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.quantity} of {self.item.title}'

    def get_total_item_price(self):
        return self.quantity * self.item.price


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateField()
    ordered = models.BooleanField(default=False)

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_total_item_price()
        return total
