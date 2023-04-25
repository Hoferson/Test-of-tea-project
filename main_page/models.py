from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Gallery(models.Model):
    
    black_text = models.CharField(max_length=20)
    orange_text = models.CharField(max_length=20)
    image = models.ImageField(upload_to='gallery_imgs')
    is_visible = models.BooleanField(default=True)
    position = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ('position', )


class About(models.Model):
    
    headline = models.CharField(max_length=50)
    text = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='about_imgs')
    is_visible = models.BooleanField(default=True)
    position = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ('position', )

    def __str__(self):
        return f'{self.headline}'
    
    
class Tea_cards(models.Model):

    title = models.CharField(max_length=30)
    price = models.PositiveSmallIntegerField()
    image = image = models.ImageField(upload_to='tea_imgs')
    is_visible = models.BooleanField(default=True)
    position = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ('position', )

    def __str__(self):
        return f'{self.title}'
    
    
class Achievements(models.Model):

     
    value = models.CharField(max_length=20)
    description = models.CharField(max_length=40)
    image = image = models.ImageField(upload_to='achievement_imgs')
    is_visible = models.BooleanField(default=True)
    position = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ('position', )

    def __str__(self):
        return f'{self.description}'
    
    
class Shop_items(models.Model):

    title = models.CharField(max_length=30)
    text = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='shop_item_imgs')
    is_visible = models.BooleanField(default=True)
    position = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ('position', )

    def __str__(self):
        return f'{self.title}'
    
    
class Questions(models.Model):

    question = models.CharField(max_length=100)
    answer = models.TextField(max_length=1000)
    is_visible = models.BooleanField(default=True)
    position = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ('position', )

    def __str__(self):
        return f'{self.question}'
    
    
class Testimonials(models.Model):

    title = models.CharField(max_length=30)
    text = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='testimonial_imgs')
    photo = models.ImageField(upload_to='client_testimonial_imgs')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    is_visible = models.BooleanField(default=True)
    position = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ('position', )

    def __str__(self):
        return f'{self.title}'
    

class Contact_us_form(models.Model):

    phone_validator = RegexValidator(regex='^\+?3?8?0?\d{2}[- ]?(\d[- ]?){7}$', 
                                     message ='Phone number is wated in "+380xx xxx xx xx" format')

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=16, validators=(phone_validator, ))
    message = models.TextField(max_length=2000)
    date_request = models.DateTimeField(auto_now_add=True)
    date_response = models.DateTimeField(auto_now=True)
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}    {self.phone}    {self.email}'

    class Meta:
        ordering = ('-date_request', )

