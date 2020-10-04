from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from blog.models import Tweeter


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        fields_classes = {'username', UserCreationForm}


class TextForm(ModelForm):
    class Meta:
        model = Tweeter
        exclude = ['created_date', 'author', 'likes']