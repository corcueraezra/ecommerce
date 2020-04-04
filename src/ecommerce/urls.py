"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

# from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin

from .views import home_page, contact_page, login_page, register_page	

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url('home/', home_page),
    # url('contact/', contact_page),
    # url('login/', login_page),
    # url('register/', register_page),
    # url('products/', product_list),

    path('admin/', admin.site.urls),
    path('home/', home_page, name='home'),
    path('contact/', contact_page, name='contact'),
    path('login/', login_page, name='login'),
    path('products/', include("products.urls", namespace="products")),
    path('register/', register_page, name='register'),
    path('search/', include("search.urls", namespace="search")),
    # path('products/', product_list),
    # path('products/<int:id>/', product_detail),
    # path('featured/', product_featured_list),
    # path('products/<slug:slug>/', product_slug_detail),
]

if settings.DEBUG:
	urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)