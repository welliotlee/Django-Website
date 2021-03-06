from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.template.defaultfilters import slugify

alphanumeric = RegexValidator(r'^[0-9a-zA-Z ]*$', 'Only alphanumeric characters are allowed.\n')

# Create your models here.
class Guide_Model(models.Model):
	name = models.CharField(max_length=256, unique=True, validators=[alphanumeric])
	author = models.CharField(max_length=128)
	#date_added = models.DateField(auto_now_add=True)
	views = models.IntegerField(default=0)
	upvotes = models.IntegerField(default=0)
	downvotes = models.IntegerField(default=0)
	desc = models.TextField()
	slug = models.SlugField()

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Guide_Model, self).save(*args, **kwargs)

	def __str__(self):
		return self.name


