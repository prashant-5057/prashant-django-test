from django.urls import path

from . import views

urlpatterns = [

    path('signup/', views.RegisterUserView.as_view(), name='user_register'),
    path('signin/', views.CutomObtainPairView.as_view(), name='user_signin'),
    path('user-details/', views.UserProfileView.as_view(), name='user_details'),
]
