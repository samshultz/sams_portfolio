from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from core.views import HomepageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', include("contact.urls"), name='contact'),
    path('', HomepageView.as_view(), name="index"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)