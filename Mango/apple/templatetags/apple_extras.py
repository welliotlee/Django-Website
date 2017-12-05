from django import template
from apple.models import Guide_Model

register = template.Library()

@register.inclusion_tag('apple/sidebar.html')
def get_sidebar_list():
	return {'guide_list' : Guide_Model.objects.all()}