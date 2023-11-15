from django.forms import ModelForm
from .models import *
from django import forms

class MemberModelForm(ModelForm):
    class Meta:
        model= Member
        
        fields = '__all__'
        #-------CHANGE THE FORM LABELS -------#
        labels = {
            'f_name':'First Name',
            'l_name': 'Last Name',
            'address':'Address',
            'age':'Age(In Years)',
            'payment': 'Payment Status',
            'package_selected':'Package Selected',
            'health_conditions': 'Health Issues( If Any)',
            'date_joined': 'Joined Date',
            'date_finish': 'Package End Date',
            'profile_pic': 'Profile Picture',
            'mobile_number': 'Contact Number',

        }
        #-----------DISPLAY DATE SELECTOR IN FORM-----------#
        widgets = {
             'date_joined': forms.DateInput(attrs={'type': 'date'}),
             'date_finish': forms.DateInput(attrs={'type': 'date'}),
        }
        #-------------------------DISPLAY 'CHOOSE OPTION ' AS DEFAULT-------#
    SEX_CHOICES_WITH_EMPTY = [('', 'Choose option')] + Member.SEX_CHOICES
    sex = forms.ChoiceField(choices=SEX_CHOICES_WITH_EMPTY) 

    PACKAGE_CHOICES_WITH_EMPTY = [('','Choose option')] + Member.PACKAGE_CHOICES
    package_selected = forms.ChoiceField(choices=PACKAGE_CHOICES_WITH_EMPTY)

    PAYMENT_CHOICES_WITH_EMPTY =[('','Choose option')] + Member.PAYMENT_STATUS
    payment = forms.ChoiceField(choices=PAYMENT_CHOICES_WITH_EMPTY)

    def clean_email(self):
        # Custom email validation to check for uniqueness and do not check for blank email field

        email = self.cleaned_data['email']                 #=>>This line retrieves the email value entered in the form after the data has been cleaned.
        
        if email and Member.objects.filter(email=email).exclude(pk=self.instance.pk).exists():#==> checks that the member field email id is same with other members and skips checking with own email.
           
            raise forms.ValidationError('This email is already in use by another member.')
        return email

    #----apply the 'input' CSS class to all the form fields in the MemberModelForm, 
    # which helps in styling the form fields consistently.------------------### 
    
    def __init__(self, *args, **kwargs):
        super(MemberModelForm, self).__init__(*args, **kwargs)

        #for single field change

        # self.fields['title'].widget.attrs.update({'class':'input','placeholder':'Add Title'})
        # self.fields['description'].widget.attrs.update({'class':'input'})
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})     

#--------if we want the email field to be blank and also unique for those who have emailid-----#    
    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     print(f"Email from form: {email}")
    #     if email:
    #         # If email is not blank, check for uniqueness
    #         existing_members = Member.objects.filter(email=email)
    #         if self.instance.pk:
    #             existing_members = existing_members.exclude(pk=self.instance.pk)
    #         print(f"Existing members: {existing_members}")
    #         if existing_members.exists():
    #             print("Email is not unique")
    #             raise forms.ValidationError('This email is already in use.')
    #     return email
        

    