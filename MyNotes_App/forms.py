from django import forms
from .models import MyNotes_Model

class MyNotes_Form(forms.ModelForm):
    class meta:
        model = MyNotes_Model
        fields = [
            
        ]