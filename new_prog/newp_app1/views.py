from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main_index(request):
	return HttpResponse("Welcome to the main index!")

def index(request):
	return HttpResponse("newp_app1 says Hello!")