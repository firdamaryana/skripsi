from django import forms
from .models import Post, Summarization

class SummarizationForm(forms.ModelForm):
	# An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Summarization
        fields = ('text',)
