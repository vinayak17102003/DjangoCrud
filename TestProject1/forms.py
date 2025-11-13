from django import forms
from .models import UserModel

class Registration(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['Name','Email','Password','Age']

        labels = {
            'Name':'User Name',
            'Email':'User Email',
            'Password':'User Password',
            'Age':'User Age'
        }
        widgets = {
            
            'Name':forms.TextInput(attrs={'placeholder':'Enter Your Name', 'class':'form-control'}),
            'Email':forms.EmailInput(attrs={'placeholder':'Enter Your Email', 'class':'form-control'}),
            'Password':forms.TextInput(attrs={'placeholder':'Enter Your Password', 'class':'form-control'}),
            'Age':forms.NumberInput(attrs={'placeholder':'Enter Your Age', 'class':'form-control'}),
        }
        
        # error_messages =
        # {
        #     'Name':{'required':'Name is Required'},
        #     'Email':{'required':'Email is Required',
        #             'invalid':'Enter a valid Email'},
        #     'Password':{'required':'Password is Required'},
        #     'Age':{'required':'Age is Required',
        #             'invalid':'Enter a valide Number'},
        # }