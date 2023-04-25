from django.shortcuts import render, redirect
from main_page.models import Contact_us_form
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required(login_url='/login/')
def contact_us_message_list(request):
    messages = Contact_us_form.objects.filter(is_processed=False)

    return render(request, 'contact_us_message_list.html', context={'messages': messages})


@login_required(login_url='/login/')
def update_message(request, pk):
    Contact_us_form.objects.filter(pk=pk).update(is_processed=True)
    return redirect('manager:messages')