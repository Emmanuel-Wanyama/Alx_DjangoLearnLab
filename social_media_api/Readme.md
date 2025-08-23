Social Media API
This document provides a guide for setting up and using the social media API. It details the steps for installation, explains the user authentication endpoints, and gives an overview of the custom user model.

Setup and Installation
Make sure you have Python and pip installed on your system.

Install the required dependencies, including Django and Django REST Framework.

pip install django djangorestframework

Navigate to the project root and run the migrations to set up the database.

python manage.py makemigrations accounts
python manage.py migrate

Start the development server.

python manage.py runserver

API Endpoints
The API provides endpoints for user management and authentication. All endpoints are located under the /api/v1/accounts/ path.

1. User Registration
URL: /api/v1/accounts/register/

Method: POST

Description: Creates a new user account and returns an authentication token.

Request Body (JSON):

username (string, required)

email (string, required)

password (string, required)

password_confirm (string, required)

bio (string, optional)

Successful Response:

201 Created

Body: {"token": "your_auth_token"}

2. User Login
URL: /api/v1/accounts/login/

Method: POST

Description: Authenticates a user and returns their authentication token.

Request Body (JSON):

username (string, required)

password (string, required)

Successful Response:

200 OK

Body: {"token": "your_auth_token"}

3. User Profile
URL: /api/v1/accounts/profile/

Method: GET or PUT

Description:

GET: Retrieves the authenticated user's profile information.

PUT: Updates the authenticated user's profile (e.g., bio or profile picture). Requires a token.

Authentication: Requires a Token in the Authorization header.

Example: Authorization: Token your_auth_token

Successful Response:

200 OK

Body: A JSON object with the user's profile details.

Custom User Model
This project uses a custom User model located in accounts/models.py. It extends Django's AbstractUser and includes the following fields:

bio: A text field for a short biography.

profile_picture: An image field for the user's profile picture.

followers: A many-to-many relationship to itself, allowing users to follow each other. The related name for following is following.