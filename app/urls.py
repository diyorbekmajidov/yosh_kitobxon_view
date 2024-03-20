from django.urls import path
from .views import (
    CreateUserView,
    PaymentUserView
    )

urlpatterns = [
    path('create/', CreateUserView.as_view(), name='create_user'),
    path("getuser/<int:pk>/", CreateUserView.as_view()),
    path("payment/", PaymentUserView.as_view(), name="pay"),
    path("paymentuser/<int:pk>/", PaymentUserView.as_view())
    ]