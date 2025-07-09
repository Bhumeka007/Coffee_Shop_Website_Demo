from django.db import models

# Coffee Categories
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
#Coffee Menu
class CoffeeItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='media/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_best_seller = models.BooleanField(default=False)
    badge = models.CharField(max_length=50, blank=True, help_text='E.g., "Top Rated", "New", "Best Value", Todays spacial"')

    def __str__(self):
        return self.name
    
#Feedback form
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"
    
#Newsletter Subscriber
class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email