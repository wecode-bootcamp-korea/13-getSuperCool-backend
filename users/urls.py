from django.urls import path
from .views      import SignUpView,LoginView,ForgotPasswordView,InquiriesView,DiscountView
urlpatterns = [
     path('/register',SignUpView.as_view()),
     path('/login',LoginView.as_view()),
     path('/forgot-password',ForgotPasswordView.as_view()),
     path('/discount',DiscountView.as_view()),
     path('/inquirie',InquiriesView.as_view())
]
