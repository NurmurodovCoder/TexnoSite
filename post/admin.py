from django.contrib import admin
from .models import Post, Author, Category, Carusel, CommentPost
from modeltranslation.admin import TranslationAdmin


# class PostAdmin(admin.ModelAdmin):
#     list_display = ("id", "title", "author", "category", "date", "like", "img")
# list_display_links = ("title",)
# fields = (
#     "title",
#     "text",
#     "img",
#     "show_image",
#     "author",
#     "category",
#     "like",
#     "read",
# )
# readonly_fields = ("show_image",)


class PostTrans(TranslationAdmin):
    list_display = ["title", "text"]
    list_display_links = ("title",)
    fields = (
        "title",
        "text",
        "img",
        "show_image",
        "author",
        "category",
        "like",
        "read",
    )
    readonly_fields = ("show_image",)


class CommentPostAdmin(admin.ModelAdmin):
    list_display = ("text", "post", "user", "date")


admin.site.register(Post, PostTrans)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Carusel)
admin.site.register(CommentPost, CommentPostAdmin)
