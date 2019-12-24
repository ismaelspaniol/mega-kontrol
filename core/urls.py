from django.urls import path
from .views import current_user, UserList, logout_user

urlpatterns = [
    path('current_user/', current_user),
    path('users/', UserList.as_view()),
    path('current_user/logout/', logout_user),
]