"""_summary_
"""
from typing import Any
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record


class SignUpForm(UserCreationForm):
    """_summary_

    Args:
        UserCreationForm (_type_): _description_
    """

    email = forms.EmailField(
        label='',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email Address',
        })
    )
    first_name = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'First Name',
        })
    )
    last_name = forms.CharField(
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Last Name',
        })
    )

    class Meta:
        """_summary_
        """
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'email', 'password1', 'password2'
        )

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """_summary_
        """
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].lable = ''
        self.fields['username'].help_text = """
            <span class="form-text text-muted">
                <small>Required. 100 characters or fewer. Letters, digits and @/./+/-/_ only.</small>
            </span>
        """

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].lable = ''
        self.fields['password1'].help_text = """<ul class="form-text text-muted small">
                <li>Your password can\'t be too similar to your other personal information.</li>
                <li>Your password must contain at least 8 characters.</li>
                <li>Your password can\'t be a commonly used password.</li>
                <li>Your password can\'t be entirely numeric.</li>
            </ul>"""

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].lable = ''
        self.fields['password2'].help_text = """<span class="form-text text-muted">
                <small>Enter the same password as before, for verificaation.</small>
            </span>
        """


class AddRecordForm(forms.ModelForm):
    """_summary_

    Args:
        forms (_type_): _description_
    """

    first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={'placeholder': 'First Name', 'class': 'form-control'}), label='')
    last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={'placeholder': 'Last Name', 'class': 'form-control'}), label='')
    email = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={'placeholder': 'Email', 'class': 'form-control'}), label='')
    phone = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={'placeholder': 'Phone Number', 'class': 'form-control'}), label='')
    address = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={'placeholder': 'Address', 'class': 'form-control'}), label='')
    city = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={'placeholder': 'City', 'class': 'form-control'}), label='')
    state = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={'placeholder': 'State', 'class': 'form-control'}), label='')
    zip_code = forms.CharField(required=True, widget=forms.widgets.TextInput(
        attrs={'placeholder': 'Zip Code', 'class': 'form-control'}), label='')

    class Meta:
        """_summary_
        """
        model = Record
        fields = ('first_name', 'last_name', 'email', 'phone',
                  'address', 'city', 'state', 'zip_code')
