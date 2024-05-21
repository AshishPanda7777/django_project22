from  django import forms 

class Topicpage(forms.Form):
    tn=forms.CharField(max_length=20)
    