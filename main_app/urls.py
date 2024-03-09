# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('create-reminder/', reminder_create_view, name='create-reminder'),
    path('reminders/', ReminderListView.as_view(), name='list-reminders'),
    path('reminder/<int:pk>/', ReminderDetailView.as_view(), name='detail-reminder'),
    path('update-reminder/<int:pk>/', reminder_update_view, name='update-reminder'),
]
