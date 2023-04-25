from django.shortcuts import render, redirect
from .models import Gallery, About, Shop_items, Tea_cards, Testimonials, Achievements, Questions
from .forms import Contact_us_form

# Create your views here.
def main_view(request):
    if request.method == 'POST':

        form_reserve = Contact_us_form(request.POST)
        if form_reserve.is_valid():
            form_reserve.save()
            return redirect('/')

    gallery = Gallery.objects.filter(is_visible=True)
    about = About.objects.filter(is_visible=True)
    shop_items = Shop_items.objects.filter(is_visible=True)
    tea_cards = Tea_cards .objects.filter(is_visible=True)
    testimonials = Testimonials.objects.filter(is_visible=True)
    achievements = Achievements.objects.filter(is_visible=True)
    questions = Questions.objects.filter(is_visible=True)
    contact_us_form = Contact_us_form()

    return render(request, 'main_page.html', context={
        'gallery':gallery, 
        'about':about,
        'shop_items': shop_items,
        'tea_cards':  tea_cards,
        'shop_items': shop_items,
        'testimonials': testimonials,
        'achievements': achievements,
        'questions': questions,
        'contact_us_form': contact_us_form,
        })

def tea_cards_view(request):

    tea_cards = Tea_cards .objects.filter(is_visible=True)

    return render(request, 'services_page.html', context={
        'tea_cards':  tea_cards,
        })

def about_view(request):

    about = About.objects.filter(is_visible=True)

    return render(request, 'about_page.html', context={
        'about': about,
        })

def teashop_view(request):

    shop_items = Shop_items.objects.filter(is_visible=True)

    return render(request, 'teashop_page.html', context={
        'shop_items': shop_items,
        })

def testimonies_view(request):

    testimonials = Testimonials.objects.filter(is_visible=True)

    return render(request, 'testimonies_page.html', context={
        'testimonials': testimonials,
        })

def contact_us_view(request):
    if request.method == 'POST':

        form_reserve = Contact_us_form(request.POST)
        if form_reserve.is_valid():
            form_reserve.save()
            return redirect('/')

    contact_us_form = Contact_us_form()

    return render(request, 'contact_us_page.html', context={
        'contact_us_form': contact_us_form,
        })