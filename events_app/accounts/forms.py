from builtins import super
from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class UserLoginForm(forms.ModelForm):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = 'Your email'
        self.fields['password'].label = 'Password'

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        username = email.split('@')[0]

        if email and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("User with this email does not exist")

            if not user.check_password(password):
                raise forms.ValidationError("This is not a correct password!")

        return super().clean(*args, **kwargs)


class UserRegisterForm(UserCreationForm):

    class Meta:
        fields = ('email', 'password1', 'password2')
        model = get_user_model()

    def clean(self, *args, **kwargs):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError("Password is not the same as Password confirmation")

        return super().clean(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].label = 'Please write your email:'
        self.fields['password1'].label = 'Please write your password:'
        self.fields['password2'].label = 'Please confirm your password:'
