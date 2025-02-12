from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('services/', views.ServiceListView.as_view(), name='services'),
    path('services/<slug:slug>/', views.ServiceDetailView.as_view(), name='service_detail'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('careers/', views.CareerListView.as_view(), name='careers'),
    path('careers/<slug:slug>/', views.JobDetailView.as_view(), name='job_detail'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]