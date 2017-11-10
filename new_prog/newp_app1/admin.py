from django.contrib import admin
from newp_app1.models import Category, Page

# Register your models here.

class PageAdmin(admin.ModelAdmin):
	fields = ('category', 'title', 'url')

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Page, PageAdmin)
admin.site.register(Category, CategoryAdmin)
