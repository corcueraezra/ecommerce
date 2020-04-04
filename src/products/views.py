from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from .models import Product

class product_list(ListView):
	queryset = Product.objects.all()
	template_name = "products/list.html"

# def product_list(request):
# 	queryset = Product.objects.all()
# 	context = {
# 		'object_list':queryset
# 	}
# 	return render(request, "products/list.html", context)

class product_detail(DetailView):
	template_name = "products/detail.html"

	def get_object(self, *args, **kwargs):
		request = self.request
		id = self.kwargs.get('id')
		instance = get_object_or_404(Product, id=id)
		return instance

# def product_detail(request, id=None):
	
# 	instance = get_object_or_404(Product, id=id)
# 	print(instance)
# 	context = {
# 		'object':instance
# 	}
# 	return render(request, "products/detail.html", context)

def product_featured_list(request):
	queryset = Product.objects.filter(featured=True)
	context = {
		'object_list':queryset
	}
	return render(request, "products/list.html", context)

def product_slug_detail(request, slug=None):
	
	instance = get_object_or_404(Product, slug=slug, active=True)
	print(instance)
	context = {
		'object':instance
	}
	return render(request, "products/detail.html", context)