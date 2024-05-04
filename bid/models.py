from django.db import models
from django.conf import settings
from django.forms import ValidationError
from django.urls import reverse

class Category(models.Model):
    field = models.CharField(max_length=64)

    def __str__(self):
        return self.field

    def get_absolute_url(self):
        return reverse('home')

class Listings(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="owned_items")
    product_name = models.CharField(max_length=64)
    description = models.CharField(max_length=2048, default='')
    date_time = models.DateTimeField(auto_now=False, auto_now_add=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)  # Modify this line
    price = models.DecimalField(max_digits=10, decimal_places=2, default="")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    closed = models.BooleanField(default=False)
    watchlist_users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="watchlist")

    def current_price(self):
        return max([bid.bid for bid in self.bids.all()] + [self.price])

    def no_of_bids(self):
        return len(self.bids.all())

    def current_winning_bidder(self):
        return self.bids.get(bid=self.current_price()).user if self.no_of_bids() > 0 else None

    def __str__(self):
        return f"{self.product_name}"

class Bid(models.Model):
    listing = models.ForeignKey(Listings, on_delete=models.CASCADE, related_name="bids")
    bid = models.DecimalField(max_digits=8, decimal_places=2)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="bids_made")

    def clean(self):
        if self.bid and self.listing.current_price():
            if self.bid <= self.listing.current_price():
                raise ValidationError({'bid': ('Your bid should be higher than the current price!')})

    def __str__(self):
        return f"Latest bid by {self.user}: ₹ {self.bid} [{self.listing}]"

class Comment(models.Model):
    post = models.ForeignKey(Listings, on_delete=models.CASCADE, related_name="comments", null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField()
    post_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.author} said: '{self.body}' [{self.post_time}]"
