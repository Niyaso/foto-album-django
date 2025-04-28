# Import necessary modules from Django
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create a custom user registration form by extending Django's built-in UserCreationForm
class CustomUserCreationForm(UserCreationForm):
    """
    A customized user registration form that extends Django's built-in UserCreationForm.
    It adds Bootstrap styling and placeholder text to the form fields.
    """

    class Meta:
        """
        Metadata for the form:
        - Links the form to Django's built-in User model.
        - Specifies that only 'username', 'password1', and 'password2' fields should be included.
        """
        model = User
        fields = ['username', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        """
        Initializes the form and customizes the widget attributes for each field
        to add CSS classes and placeholder text for better UI/UX.
        """
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control', 
            'placeholder': 'Enter username...'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control', 
            'placeholder': 'Enter password...'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control', 
            'placeholder': 'Confirm password...'
        })
