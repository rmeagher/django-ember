from django.contrib import admin
from django.urls import path
from .views import BookAPIView, BookRudView


urlpatterns = [
    path('', BookAPIView.as_view(), name='book-create'),
    path('<int:id>/', BookRudView.as_view(), name='book-rud')
]
