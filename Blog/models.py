from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
	#creating the models 
	author = models.ForeignKey('auth.User')
	topic = models.CharField(max_length=300)
	article = models.TextField()
	created_date = models.DateTimeField(default= timezone.now)
	pubished_date = models.DateTimeField(blank=True)
	image = models.ImageField(upload_to='img/%y/%m/%d')

	def published_date(self):
		# no call return the publih time
		published_date = timezone.now
		published_date.save()

	def Meta():
		ordering = '-pk'
	def __str__(self):
		return self.topic


