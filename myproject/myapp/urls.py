from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('management', views.management, name='management'),  # เพิ่ม name='management'
    path('forms', views.forms, name='forms'),  # เพิ่ม name='forms'
    path('edit/<product_id>', views.edit, name='edit'),
    path('delete/<product_id>', views.delete, name='delete')]