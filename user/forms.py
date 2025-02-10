from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile,USER_TYPES_CHOICES

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    user_type = forms.ChoiceField(choices=USER_TYPES_CHOICES)

    class meta:
        model = User
        fields = ('username','email','password1','password2','user_type')

        def save(self, commit=True):
            user = super().save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
                user.userprofile.user_type = self.cleaned_data['user_type']
                user.userprofile.save()
            return user
        
    class ProfileUpdateForm(forms.ModelForm):
        class Meta:
            model = UserProfile
            fields = ['contact_info','address','organization_name']