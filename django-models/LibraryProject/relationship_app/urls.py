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
<<<<<<< HEAD
from . import views # Import the entire views module
=======
from . import views # Changed: Import the entire views module
>>>>>>> 0e957cfa55ee3d307007742541c31dbc68577a6c
from django.contrib.auth import views as auth_views # Import Django's built-in auth views

app_name = 'relationship_app' # Define app_name for namespacing

urlpatterns = [
<<<<<<< HEAD
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='relationship_app:logged_out'), name='logout'),
    path('register/', views.register, name='register'),
=======
    path('books/', views.list_books, name='list_books'), # Changed to views.list_books
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'), # Changed to views.LibraryDetailView

    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='relationship_app:logged_out'), name='logout'), # Redirects to 'logged_out' URL
    path('register/', views.register, name='register'), # Changed to views.register
>>>>>>> 0e957cfa55ee3d307007742541c31dbc68577a6c

    # A simple page to show after logout
    path('logged_out/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logged_out'),
    
    # A simple page to redirect to after successful login/registration
<<<<<<< HEAD
    path('login_success/', views.list_books, name='login_success'),

    # Role-based access URLs
    path('admin_dashboard/', views.admin_view, name='admin_dashboard'),
    path('librarian_dashboard/', views.librarian_view, name='librarian_dashboard'),
    path('member_dashboard/', views.member_view, name='member_dashboard'),
=======
    # You can change this to a more meaningful page later, e.g., a user profile or dashboard
    path('login_success/', views.list_books, name='login_success'), # Changed to views.list_books
>>>>>>> 0e957cfa55ee3d307007742541c31dbc68577a6c
]

