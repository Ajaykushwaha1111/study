from django import forms
from django.contrib.auth.models import User
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'




class SignupForm(forms.ModelForm):
    class Meta:
        model =User
        fields =('username','email',"password")
    username =forms.CharField(max_length=50,help_text="")
    password = forms.CharField(widget=forms.PasswordInput,max_length=20,min_length=8)

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    # def clean_username(self):
    #     username = self.cleaned_data.get('username')
    #     if "" not in username:
    #         raise forms.ValidationError("Username not valid !")
    #     return username