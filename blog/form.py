from django import forms

class BlogForm(forms.Form):
	name = forms.CharField(max_length=100)
	institute = forms.CharField(max_length=100)
	title = forms.CharField(max_length=100)
	content = forms.CharField(widget=forms.Textarea)
	image = forms.ImageField()