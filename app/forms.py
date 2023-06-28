from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm


class CustomUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name',
                  'last_name', 'password1', 'password2']

        labels = {
            'first_name': 'Ism',
            'last_name': 'Familya',
            'email': 'E-pochta',
            'username': 'Login',
        }

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)

        for key, field in self.fields.items():
            field.widget.attrs.update({'class': 'input input--text'})
