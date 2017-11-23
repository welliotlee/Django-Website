from django import forms
#from django.contrib.auth.models import User
from apple.models import Guide_Model

class GuideForm(forms.ModelForm):
	name = forms.CharField(max_length=256, help_text="Please enter your guide's name:")
	author = forms.CharField(max_length=128, help_text="Placeholder Author:")
	desc = forms.CharField(widget=forms.Textarea, help_text="Enter your guide description here:")
	#date_added = forms.DateField(widget=forms.HiddenInput())
	views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	upvotes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	downvotes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	slug = forms.CharField(widget=forms.HiddenInput(), required=False)

	class Meta:
		model = Guide_Model
		exclude = ('views', 'upvotes', 'downvotes', 'slug', )