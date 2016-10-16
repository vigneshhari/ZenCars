from django import forms

class DocumentForm(forms.Form):
	photolinks = forms.FileField(label='photolinks')
	videolink = forms.CharField(label='videolink', max_length=200)
	review = forms.CharField(label='review')

