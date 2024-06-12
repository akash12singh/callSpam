from django.urls import path
from . import views
from .views import UserRegistration, UserLogin, ContactSearch, PhoneSearch, UserViewSet




urlpatterns = [
    # User endpoints
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    # Contact endpoints
    path('contacts/', ContactSearch.as_view(), name='contact-search'),
    path('contacts/<int:pk>/', views.ContactDetail.as_view(), name='contact-detail'),
    path('contacts/search/', ContactSearch.as_view(), name='contact_search'),
    path('contacts/phonesearch/', PhoneSearch.as_view(), name='phone_search'),
    # Spam endpoints
    path('spam/', views.SpamViewSet.as_view({'get': 'list', 'post': 'create'}), name='spam-list'),
    path('spam/<int:pk>/', views.SpamViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='spam-detail'),
    #Login and Registration
    path('register/', UserRegistration.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='login'),
]
