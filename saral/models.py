from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.


		 
class Category(models.Model):
	cat_choice = [
		('Movie','Movie'),
		('Show','Show'),
		('Series','Series'),
	]
	name = models.CharField(choices=cat_choice, max_length=20, null=False, blank=False)

	def __str__(self):
		return self.name

class Genres(models.Model):
	name = models.CharField(max_length=20, null=False, blank=False)

	def __str__(self):
		return self.name

class New(models.Model):
	name =models.CharField(max_length=20,blank=False, null=False)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	contentAge =models.CharField(max_length=20,blank=False, null=False)
	description =models.TextField(max_length=2000,blank=False, null=False)
	source_vid =models.CharField(max_length=2000,blank=False, null=False)
	starring =models.CharField(max_length=200,blank=False, null=False)
	genres = models.ManyToManyField(Genres, related_name='genres1')
	tag = models.ManyToManyField(Genres, related_name='genres2')
	image = models.ImageField(upload_to="Poster/")
	publishDate = models.DateField()

	def __str__(self):
		return self.name

class Rating(models.Model):
	content_id = models.IntegerField(blank=True, null=True)
	comments = models.TextField(max_length=200, blank=True, null=True)
	rating_number = models.IntegerField(blank=False)
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.user.username

class Customer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
	image = models.ImageField(upload_to="user_image/", null=True, blank=True)
	dob = models.DateField()

	def __str__(self):
		return self.user.username


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		Customer.objects.create(user=instance)
