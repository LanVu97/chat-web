from django import forms

from .models import Profile

class UpdateProfileForm(forms.ModelForm):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    image = forms.ImageField(widget=forms.FileInput(attrs={'id': 'photo'}))
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)  

    class Meta:
        model = Profile
        fields = ['username', 'image', 'gender', 'country']