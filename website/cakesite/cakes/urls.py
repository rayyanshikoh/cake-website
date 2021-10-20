from django.urls import path
from . import views

app_name = 'cakes'
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:cake_id>/', views.detail, name='detail'),
    path('<int:cake_id>/order/', views.order, name='order'),
    path('<int:cake_id>/order/comporder', views.comporder, name='comporder'),
]