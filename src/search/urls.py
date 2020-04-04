from django.urls import path

from .views import (
    product_list, 
    product_detail,
    product_featured_list,
    product_slug_detail,
    )
app_name = 'products'
urlpatterns = [
    path('', product_list.as_view(), name='list'),
    path('<int:id>/', product_detail.as_view()),
    path('featured/', product_featured_list),
    path('<slug:slug>/', product_slug_detail, name='detail'),
]

