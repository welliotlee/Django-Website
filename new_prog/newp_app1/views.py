from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):

	context_dict = {'boldmessage': "I am bold font from the context"}
	return render(request, 'newp_app1/index.html', context_dict)

def about(request):
	return render(request, 'newp_app1/about.html')