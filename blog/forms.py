from django import forms
from .models import Summarization

class SummarizationForm(forms.ModelForm):
	# An inline class to provide additional information on the form.
    PILIHAN=(
            (1,1),
            (2,2),
            )
    jumlah = forms.ChoiceField(choices=PILIHAN)
    text = forms.CharField(widget=forms.Textarea, error_messages={'required': 'Teks Tidak Boleh Kosong!'})
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Summarization
        fields = ('text',)
