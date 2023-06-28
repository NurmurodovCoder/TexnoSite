from .models import Post
from django.forms import ModelForm

from modeltranslation.forms import TranslationModelForm


class PostForm(TranslationModelForm):
    class Meta:
        model = Post
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)

        for key, field in self.fields.items():
            field.widget.attrs.update({"class": "input input--text"})


class PostFormCreated(TranslationModelForm):
    class Meta:
        model = Post
        fields = ["title", "text", "category", "img"]

    def __init__(self, *args, **kwargs):
        super(TranslationModelForm, self).__init__(*args, **kwargs)

        for key, field in self.fields.items():
            field.widget.attrs.update({"class": "input input--text"})
