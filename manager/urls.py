from django.urls import path
from .views import contact_us_message_list, update_message

app_name = 'manager'

urlpatterns = [
    path('messages/', contact_us_message_list, name='messages'),
    path('messages/update/<int:pk>/', update_message, name='update_message')
]