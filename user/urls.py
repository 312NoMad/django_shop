

from django.urls import path

from .views import UserList, SignUp, Login, TokenRefresh, UserView, UserUpdate


urlpatterns = [
    path('', UserList.as_view()),
    path('signup/', SignUp.as_view()),
    path('login/', Login.as_view()),
    path('token/', TokenRefresh.as_view()),
    path('user/', UserView.as_view()),
    path('update/<int:pk>/', UserUpdate.as_view())
]
