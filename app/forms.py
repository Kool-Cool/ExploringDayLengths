from django import forms

# creating a form 
from .models import User


class  DaylightHours(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        
        
        
        
    # date = forms.DateField( required=True)
    # latitude_south = forms.IntegerField( required=True)
