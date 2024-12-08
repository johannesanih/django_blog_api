# django_blog_api
A RESTful API built with Django and Django REST Framework for managing blog posts. It allows users to create, view, like, and delete posts. Includes user authentication, custom permissions, and a like system. Designed to give users full control over their blog posts while enforcing security and ownership.

Blog API
This project is a RESTful API built with Django and Django REST Framework (DRF) that allows users to create and manage 

blog posts. It supports features such as creating, viewing, and liking blog posts, as well as managing user accounts.

Features
User 

Authentication: Allows users to sign in and manage blog posts.
Blog Post Management: Users can create, view, update, and delete 

blog posts.
Like System: Users can "like" a blog post, which increments the like count.
Custom Permissions: Only the owner of a blog 

post can modify it. Other users can view but not alter posts.
Technologies Used
Django
Django REST Framework
SQLite (default 

database, can be replaced with PostgreSQL or other)
Python 3.x
Installation
Clone the repository:

bash
Copy code
git clone 

https://github.com/yourusername/blog-api.git
cd blog-api
Create and activate a virtual environment:

bash
Copy code
python3 -m 

venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install the required dependencies:

bash
Copy code
pip 

install -r requirements.txt
Apply migrations:

bash
Copy code
python manage.py migrate
Create a superuser (to access the Django 

admin panel):

bash
Copy code
python manage.py createsuperuser
Follow the prompts to create an admin user.

Run the development 

server:

bash
Copy code
python manage.py runserver
The API will be available at http://127.0.0.1:8000/.

API Endpoints
Blog Posts
GET 

/blogposts/ - List all blog posts.
POST /blogposts/ - Create a new blog post.
GET /blogposts/{id}/ - Retrieve a single blog post.
PUT 

/blogposts/{id}/ - Update a specific blog post (only if you're the owner).
DELETE /blogposts/{id}/ - Delete a specific blog post (only if 

you're the owner).
POST /blogposts/{id}/like/ - Increment the "like" count of a blog post.
Users
GET /users/ - List all users.
POST 

/users/ - Create a new user account.
GET /users/{id}/ - Retrieve a specific user's details.
Permissions
IsAuthenticated: All endpoints 

require authentication.
IsOwnerOrReadOnly: Only the owner of a blog post can modify it (update or delete). Other users can only 

view it.
Example Requests
1. Create Blog Post (POST /blogposts/)
json
Copy code
{
    "title": "My First Blog Post",
    "content": "This is 

the content of my first blog post."
}
2. Like Blog Post (POST /blogposts/{id}/like/)
No body needed, just a POST request to like a blog 

post.

3. Get Blog Post Details (GET /blogposts/{id}/)
json
Copy code
{
    "id": 1,
    "title": "My First Blog Post",
    "content": "This is the 

content of my first blog post.",
    "owner": 1,
    "likes": 5
}
Testing
You can run tests for this API by running:

bash
Copy code
python 

manage.py test
This will run all the tests for the app and verify that your endpoints are working as expected.

License
This project is 

licensed under the MIT License - see the LICENSE file for details.
