from django.shortcuts import render
from apple.forms import GuideForm
import datetime
from apple.models import Guide_Model

# Create your views here.
def home(request):
	context_dict = {}
	return render(request, 'apple/homepage.html', context_dict)

def faq(request):
	context_dict = {}
	return render(request, 'apple/faq.html', context_dict)

def guide(request, guide_name_slug):
	context_dict = {}
	try:
		guide = Guide_Model.objects.get(slug=guide_name_slug)
		context_dict['guide'] = guide
	except Guide_Model.DoesNotExist:
		pass
	return render(request, 'apple/guide.html', context_dict)

def add_guide(request):

	if request.method == 'POST':
		form = GuideForm(request.POST)
		if form.is_valid():
			guide = form.save(commit=False)
			guide.save()
			return home(request)
		else:
			print(form.errors)
	else:
		form = GuideForm()

	context_dict = {'form':form}

	return render(request, 'apple/add_guide.html', context_dict)

def list_guides(request):
	context_dict = {}
	guide_list = Guide_Model.objects.order_by('views')[:]
	context_dict = {'guide_list' : guide_list, }
	return render(request, 'apple/list_guides.html', context_dict)

def rate_guides(request):
	context_dict = {}
	guide_list = Guide_Model.objects.order_by('views')[:]
	context_dict = {'guide_list' : guide_list, }
	return render(request, 'apple/rate_guides.html', context_dict)