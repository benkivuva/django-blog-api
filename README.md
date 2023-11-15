# Django Blog API

Welcome to the Django Blog API, a powerful tool for managing blog content. This README provides comprehensive information on the API's authentication and blog-related endpoints.

## Authentication Endpoints

### Authenticate User (POST)

- **Endpoint:** `/auth/login/`
- **View:** `auth_login_create`
- **Description:** Authenticate an existing user.
- **Request Body:**
  ```json
  {
    "username": "your_username",
    "password": "your_password"
  }
  ```

### Register User (POST)

- **Endpoint:** `/auth/register/`
- **View:** `auth_register_create`
- **Description:** Register a new user.
- **Request Body:**
  ```json
  {
    "username": "new_username",
    "first_name": "first_name",
    "last_name": "last_name",
    "password": "new_password"
  }
  ```

## Blog Endpoints

### List Blogs (GET)

- **Endpoint:** `/blogs/`
- **View:** `blogs_list`
- **Description:** Retrieve a list of all blog posts.

### Create Blog (POST)

- **Endpoint:** `/blogs/`
- **View:** `blogs_create`
- **Description:** Create a new blog post.
- **Request Body:**
  ```json
  {
    "title": "Blog Title",
    "content": "Blog Content"
  }
  ```

### Read Blog (GET)

- **Endpoint:** `/blogs/{id}/`
- **View:** `blogs_read`
- **Description:** Retrieve details of a specific blog post.

### Update Blog (PUT)

- **Endpoint:** `/blogs/{id}/`
- **View:** `blogs_update`
- **Description:** Update a specific blog post.
- **Request Body:**
  ```json
  {
    "title": "Updated Title",
    "content": "Updated Content"
  }
  ```

### Partial Update Blog (PATCH)

- **Endpoint:** `/blogs/{id}/`
- **View:** `blogs_partial_update`
- **Description:** Partially update a specific blog post.
- **Request Body:**
  ```json
  {
    "content": "Updated Content"
  }
  ```

### Delete Blog (DELETE)

- **Endpoint:** `/blogs/{id}/`
- **View:** `blogs_delete`
- **Description:** Delete a specific blog post.

## Getting Started

1. Clone the repository: `git clone https://github.com/benkivuva/django-blog-api.git`
2. Navigate to the project directory: `cd django-blog-api`
3. Set up a virtual environment: `python -m venv venv`
4. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`
5. Install dependencies: `pip install -r requirements.txt`
6. CD blogapi/
7. Apply migrations: `python manage.py migrate`
8. Run the development server: `python manage.py runserver`

Now, the Django Blog API is up and running. You can access the API endpoints as described above.

## Documentation

For detailed documentation on each endpoint, including request and response formats, explore the Swagger documentation. Start the development server and visit `http://127.0.0.1:8000/swagger/` in your browser.

## Contributions

Contributions to enhance the functionality and features of the Django Blog API are welcome. Feel free to fork the repository, make your changes, and submit a pull request.

Happy coding!
