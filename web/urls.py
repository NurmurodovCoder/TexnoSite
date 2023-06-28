from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

admin.site.site_header = "TexnoBlog admin paneli"
admin.site.site_title = "TexnoBlog admin paneli"
admin.site.index_title = "TexnoBlog admin paneli"

urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
]

urlpatterns += i18n_patterns(
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path("admin/", admin.site.urls),
    path("account/", include("app.urls")),
    path("", include("post.urls")),
    path("accounts/", include("allauth.urls")),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# from django.contrib.sites.models import Site

# sites = Site()
# sites.domain = "http://127.0.0.1:8000/"
# sites.save()
# print(sites.id)
