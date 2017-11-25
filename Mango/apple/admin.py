from django.contrib import admin
from apple.models import Guide_Model


# Register your models here.
class GuideAdmin(admin.ModelAdmin):
	fields = ('name', 'author', 'desc', 'views', 'upvotes', 'downvotes', 'slug')

admin.site.register(Guide_Model, GuideAdmin)