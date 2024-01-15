from django import forms

from .models import Artist

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name']
        # widgets = {
        #     'name': forms.TextInput()
        # }

# class SearchPropertyForm(forms.Form):

#     property_type = forms.ModelChoiceField(label=_("Property Type"), 
#                                            queryset=HouseType.objects.all(),
#                                            widget=forms.Select
#                                            (attrs={'class':'form-control input-sm'}))
#     location = forms.ModelChoiceField(label=_('Location'), 
#                                       queryset=HouseLocation.objects.all(), 
#                                       widget=forms.Select(
#                                           attrs={'class':'form-control input-sm'}))