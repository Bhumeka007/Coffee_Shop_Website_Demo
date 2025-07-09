from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Feedback, NewsletterSubscriber

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscriber
        fields = ['email']

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        #Username
        self.fields['username'].help_text = ''
        self.fields['username'].label = 'Username *'

        #Email
        self.fields['email'].help_text = ''
        self.fields['email'].label = 'Email *'

        #Password1
        self.fields['password1'].help_text = 'Use 7 to 13 Characters'
        self.fields['password1'].label = "Password *"

        #Password1
        self.fields['password2'].help_text = ''
        self.fields['password2'].label = 'Confirm  Password *'

    def clean_password1(self):
        password = self.cleaned_data.get('password1')
        if len(password) < 7 or len(password) > 13:
            raise forms.ValidationError("Are you Blind?")
        return password
