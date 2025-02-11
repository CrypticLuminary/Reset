from django import forms
from .models import PostWasteDetails

class PostWasteDetailsForm(forms.ModelForm):
    class Meta:
        model = PostWasteDetails
        fields = ['description', 'image', 'category', 'price']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'})
        }