from django.contrib import admin
from django.urls import path
from core.views import first_page
from core.views import second_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first_page/', first_page),
    path('second_page/', second_page)
]
