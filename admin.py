from django.contrib import admin
from .models import Category, CoffeeItem, Feedback, NewsletterSubscriber

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(CoffeeItem)
class CoffeeItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_best_seller', 'badge')
    list_filter = ('category', 'is_best_seller')
    search_fields = ('name', 'description')

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')

@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')
    search_fields = ('email',)