from django.urls import path,include
from .views import main, hi


urlpatterns = [
    path('', hi),
    path('main', main),
]