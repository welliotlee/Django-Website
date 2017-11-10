from django.contrib import admin
from newp_app1.models import Category, Page

# Register your models here.
admin.site.register(Category)

class PageAdmin(admin.ModelAdmin):
	fields = ('category', 'title', 'url')

admin.site.register(Page, PageAdmin)