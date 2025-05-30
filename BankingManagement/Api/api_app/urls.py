from django.urls import path
from .views import DataAPIView, index

app_name='api_app'

urlpatterns = [
    path('', index, name='index'),
    path('data/', DataAPIView.as_view(), name='data-api'),
]