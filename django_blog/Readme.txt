Authentication Documentation
This documentation explains how the authentication system works in your Django blog project. It covers user registration, login, and profile management.

How Authentication Works
The system uses Django’s built-in authentication for core functions and custom views for registration and profile management.

Registration: A custom view, register, handles new user creation. It uses a UserRegisterForm to validate user input. Once valid, it creates a new User object in the database.

Login: The system uses Django’s built-in LoginView. This view handles the form submission, validates user credentials against the database, and creates a session for the user.

Logout: The LogoutView ends the user's session and redirects them. No custom code is needed.

Profile Management: A custom view, profile, handles changes to a user's account. It uses two forms: UserUpdateForm for fields like username and email and ProfileUpdateForm for the profile picture. It updates both the User and Profile models simultaneously.

How to Test Each Feature
You can test each feature by accessing the correct URL in your browser while your development server is running.

Register a User:

Go to http://127.0.0.1:8000/register/.

Fill out the form with a unique username and a valid email.

Click Sign Up.

A success message will appear, and you will be redirected to the login page.

Log In:

Go to http://127.0.0.1:8000/accounts/login/.

Enter the username and password you just created.

Click Log In.

You will be redirected to the home page or another default page.

Manage Profile:

While logged in, go to http://127.0.0.1:8000/profile/.

Change your username or email in the form.

You can also upload an image for your profile.

Click Update. A success message will confirm the changes.

Log Out:

Go to http://127.0.0.1:8000/accounts/logout/.

You will be logged out and redirected to a confirmation page.