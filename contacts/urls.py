from django.urls import path

from . import views


urlpatterns = [
    path('contact', views.contact, name='contact'),
    # path('edit_contact', views.edit_contact, name='edit_contact'),
]
