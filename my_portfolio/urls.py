from django.contrib import admin
from django.urls import path

from core.views import HomepageView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', HomepageView.as_view(), name="index"),
]
