from django import forms

class PasteForm(forms.Form):
    title = forms.CharField(max_length=125,required=True,widget=forms.Textarea(attrs={'style':'width:10%;height:3%'}))
    language = forms.CharField(max_length=15,widget=forms.Textarea(attrs={'style':'width:10%;height:3%'}))
    snippet = forms.CharField(widget=forms.Textarea(attrs={'style':'width:100%;height:90% ','rows':1,'cols':1}))
    