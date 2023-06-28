from .models import Post, Carusel, Category
from modeltranslation.translator import TranslationOptions, register


@register(Post)
class PostTranslation(TranslationOptions):
    fields = ("title", "text")


@register(Carusel)
class CaruselTranslation(TranslationOptions):
    fields = ("title", "body")


# @register(Category)
# class CategoryTranslation(TranslationOptions):
#     fields = ("name",)
