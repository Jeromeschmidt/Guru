from django.forms import ModelForm
from guru.users.models import User


class UserForm(ModelForm):
    """ Render and process a form based on the Page model. """
    model = User
