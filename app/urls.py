from django.urls import path
from .views import (
    CreateUserView)

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create_user'),
    path("getuser/<int:pk>/", CreateUserView.as_view())
    ]