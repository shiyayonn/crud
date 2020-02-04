from django import forms 
from cars.models import Car
class CarForm(forms.ModelForm):  
    class Meta:  
        model = Car
        fields = "__all__"  

class EditForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ["cname","ccolor"]

class MoveForm(forms.Form):
    sid = forms.CharField(label="sid",max_length=20)

class FilterForm(forms.Form):
    fcolor = forms.CharField(label="fcolor",max_length=20)