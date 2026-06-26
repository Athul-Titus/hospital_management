from django.urls import path
from.import views

urlpatterns = [
    path('index', views.index,name = "index "),
    path('data', views.data,name = "data"),
    path('home', views.home ,name = "home"),
    path('about', views.about , name = "about"),
    path('details', views.details , name = "details"),
    path('departments', views.departments_view, name = "departments"),
    path('doctors', views.doctors_view, name = "doctors"),
    path('booking', views.booking_view, name = "booking"),
    path('bookings', views.bookings_list_view, name = "bookings"),
]
