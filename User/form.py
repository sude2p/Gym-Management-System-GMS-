from django import forms

from django.contrib.auth.models import User

class UserModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields =['username','password']
        # labels = {
        #     'name': 'Full Name'
        # }
    def __init__(self, *args, **kwargs):
        super(UserModelForm, self).__init__(*args, **kwargs)

        # Set the password field widget to PasswordInput
        self.fields['password'].widget = forms.PasswordInput()