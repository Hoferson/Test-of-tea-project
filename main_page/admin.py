from django.contrib import admin
from .models import Gallery, About, Shop_items, Tea_cards, Testimonials, Achievements, Questions, Contact_us_form


@admin.register(Gallery)
class GallaryAdmin(admin.ModelAdmin):
    list_display = ['black_text', 'orange_text', 'position', 'is_visible']
    list_filter = ['is_visible']


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['headline', 'position', 'is_visible']
    list_filter = ['is_visible']


@admin.register(Shop_items)
class Shop_itemsAdmin(admin.ModelAdmin):
    list_display = ['title', 'position', 'is_visible']
    list_filter = ['is_visible']


@admin.register(Tea_cards)
class Tea_cardsAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'position', 'is_visible']
    list_filter = ['is_visible']


@admin.register(Testimonials)
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ['title', 'first_name', 'surname', 'position', 'is_visible']
    list_filter = ['is_visible']


@admin.register(Achievements)
class AchievementsAdmin(admin.ModelAdmin):
    list_display = ['value', 'description', 'position', 'is_visible']
    list_filter = ['is_visible']


@admin.register(Questions)
class QuestionsAdmin(admin.ModelAdmin):
    list_display = ['question', 'position', 'is_visible']
    list_filter = ['is_visible']
    

@admin.register(Contact_us_form)
class Contact_us_formAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'date_request', 'is_processed']
    list_filter = ['is_processed']