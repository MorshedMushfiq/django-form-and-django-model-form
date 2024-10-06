from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your Name", widget=forms.TextInput(attrs={
        "placeholder": "Your Full Name",
        "class": "form-control" #add custom css classes if needed.
        
        
    }))
    email =  forms.EmailField(label="Email", widget=forms.TextInput(attrs={
        'placeholder': "Your Email Address",
        "class": "form-control"
    }))
    dept =  forms.CharField(label="Department", widget=forms.TextInput(attrs={
        'placeholder': "Your Department",
        "class": "form-control"
    }))



