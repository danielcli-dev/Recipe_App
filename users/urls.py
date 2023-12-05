from django.urls import path
from .views import UserListView, UserDetailView

app_name = 'users' 

urlpatterns = [
   path('users/', UserListView.as_view(), name='list'),
   path('users/<pk>', UserDetailView.as_view(), name='detail')
]

