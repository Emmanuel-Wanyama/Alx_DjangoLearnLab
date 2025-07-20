"""
URL configuration for LibraryProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import list_books, LibraryDetailView, register # Import register view
from django.contrib.auth import views as auth_views # Import Django's built-in auth views

app_name = 'relationship_app' # Define app_name for namespacing

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='relationship_app:logged_out'), name='logout'), # Redirects to 'logged_out' URL
    path('register/', register, name='register'), # Use the custom register view

    # A simple page to show after logout
    path('logged_out/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logged_out'),
    
    # A simple page to redirect to after successful login/registration
    # You can change this to a more meaningful page later, e.g., a user profile or dashboard
    path('login_success/', list_books, name='login_success'), # Example: redirect to book list after login/register
]
