from django import forms

class HashForm(forms.Form):
    text = forms.CharField(label='Enter hash here:',widget=forms.Textarea)
