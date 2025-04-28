from django.urls import path
from . import views

# Define URL patterns for the app
urlpatterns = [
    # Authentication URLs
    path('login/', views.loginUser, name="login"),     # URL for user login
    path('logout/', views.logoutUser, name="logout"),   # URL for user logout
    path('register/', views.registerUser, name="register"),  # URL for user registration

    # Main application URLs
    path('', views.gallery, name='gallery'),            # URL for the main gallery page
    path('photo/<str:pk>/', views.viewPhoto, name='photo'),  # URL for viewing a single photo by its primary key (pk)
    path('add/', views.addPhoto, name='add'),            # URL for adding/uploading a new photo
]
