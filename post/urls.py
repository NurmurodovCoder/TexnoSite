from django.urls import path, include
from .views import (
    post,
    post_get,
    post_edit,
    post_delete,
    post_create,
    category_post,
    search,
)

urlpatterns = [
    path("", post, name="post"),
    path("post_get/<int:id>/", post_get, name="post_get"),
    path("post_create/", post_create, name="post_create"),
    path("post_edit/<int:id>/", post_edit, name="post_edit"),
    path("post_delete/<int:id>/", post_delete, name="post_delete"),
    path("category_post/<str:category>/", category_post, name="category_post"),
    path("search/", search, name="search"),
]
