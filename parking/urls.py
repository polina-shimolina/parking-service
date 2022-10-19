from django.contrib import admin
from django.urls import path
from parking_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('parklist/', views.parkList, name='parks_url'),
    path('', views.hello),
    path('parking/<int:id>/', views.GetParking, name='park_url'),

]
