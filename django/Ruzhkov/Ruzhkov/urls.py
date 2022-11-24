from django.contrib import admin
from django.urls import path

from kostya import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, kwargs = {'name': 'Kostya', 'fname': 'Ruzhkov', }),
    path('about', views.about, kwargs = {'about': 'Приехал с Чебоксар'}),
    path('contact', views.contact, kwargs = {'phone': '+79373970772'}),

]
