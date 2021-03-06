import uuid
import os
from django.db import models
from django.db.models.signals import pre_save,post_save
from .utils import unique_slug_generator
from django.urls import reverse

def get_file_path(instance, filename):
	ext = filename.split('.')[-1]
	filename = "%s.%s" % (uuid.uuid4(), ext)
	return os.path.join('products/', filename)

# def get_filename_ext(filepath):
# 	base_name = os.path.basename(filepath)
# 	name, ext = os.path.splitext(base_name)
# 	return name, ext

# def upload_image_path(instance, filename):
# 	print(instance)
# 	print(filename)
# 	new_filename = random.randint(1, 8342233)
# 	name, ext = get_filename_ext(filename)
# 	final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
# 	return "products/{new_filename}/{final_filename}".format(
# 		new_filename=new_filename,
# 		final_filename=final_filename
# 		)

class Product(models.Model):
	title 		= models.CharField(max_length=120)
	slug		= models.SlugField(unique=True, blank=True)
	description = models.TextField()
	price 	 	= models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
	image		= models.FileField(upload_to=get_file_path, null=True, blank=True)
	featured	= models.BooleanField(default=False)
	active		= models.BooleanField(default=True)
	timestamp	= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		# return "/products/{slug}/".format(slug=self.slug)
		return reverse("products:detail", kwargs={"slug": self.slug})

def product_pre_save_receiver(sender,instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product)